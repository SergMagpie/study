from odoo import fields, models, api, _
from odoo.exceptions import UserError


class PatientVisit(models.Model):
    _name = "hr_hospital.patient_visit"
    _description = "Patient Visit"

    active = fields.Boolean(
        string="Active",
        default=True,
    )
    visit_date = fields.Date(
        string="Visit Date",
    )
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string="Doctor",
    )
    patient_id = fields.Many2one(
        comodel_name='hr_hospital.patient',
        string="Patient",
    )
    disease_id = fields.Many2one(
        comodel_name='hr_hospital.disease',
        string="Disease",
    )
    visit_status = fields.Selection(
        selection=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')],
        string="Visit Status",
    )
    visit_planned_datetime = fields.Datetime(
        string="Planned date and time of the visit",
        help="Planned date and time of the visit "
             "(to plan the doctor's appointment schedule)",
    )
    visit_real_datetime = fields.Datetime(
        string="Date and time when the visit took place",
    )
    diagnosis_ids = fields.One2many(
        comodel_name='hr_hospital.diagnosis',
        inverse_name='visit_id',
        string="Diagnosis",
    )
    name = fields.Char(
        string="Patient Name",
        related="patient_id.name",
    )

    _sql_constraints = [('date_uniq',
                         "unique(doctor_id, patient_id, visit_planned_datetime)",
                         "One patient cannot be booked with the same doctor "
                         "more than once on the same day!")]

    def unlink(self):
        if self.diagnosis_ids:
            raise UserError(_('It is forbidden to delete or archive visits with diagnoses!'))
        res = super().unlink()
        return res

    def write(self, vals):
        if 'active' in vals and not vals['active'] and self.diagnosis_ids:
            raise UserError(_('It is forbidden to delete or archive visits with diagnoses!'))
        res = super().write(vals)
        if 'visit_status' in vals and vals['visit_status'] == 'completed':
            if not self.diagnosis_ids:
                raise UserError(_('It is forbidden to complete visits without diagnoses!'))
            if self.doctor_id.is_intern and not all(self.diagnosis_ids.mapped('is_confirmed')):
                raise UserError(_('It is forbidden to complete visits by doctor intern without confirmation!'))
        return res

    @api.onchange('visit_planned_datetime')
    def _onchange_planned_datetime(self):
        self.visit_date = self.visit_planned_datetime
