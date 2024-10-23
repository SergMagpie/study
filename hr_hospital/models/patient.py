from odoo import fields, models


class Patient(models.Model):
    _name = "hr_hospital.patient"
    _description = "Patient"
    _inherit = "hr_hospital.person"

    personal_doctor_id = fields.Many2one(
        comodel_name="hr_hospital.doctor",
        string="Personal doctor",
    )

    date_of_birth = fields.Date(
        string="Date of Birth",
    )

    age = fields.Integer(
        string="Age",
        compute="compute_age",
    )

    passport_data = fields.Char(
        string="Passport data",
    )

    contact_person_id = fields.Many2one(
        comodel_name="res.partner",
        string="Contact Person",
    )
    diagnosis_ids = fields.One2many(
        comodel_name="hr_hospital.diagnosis",
        string="Diagnosis",
        compute='_compute_diagnosis',
    )
    last_visit_state = fields.Selection(
        selection=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')],
        string="Visit Status",
        compute='compute_last_visit_state',
    )

    def _compute_diagnosis(self):
        """necessary method for hospital"""
        for record in self:
            record.diagnosis_ids = [(6, 0, record.env['hr_hospital.patient_visit'].search(
                [('patient_id', '=', record.id)]).diagnosis_ids.ids)]

    def compute_age(self):
        """necessary method for hospital"""
        for record in self:
            if record.date_of_birth:
                record.age = (fields.Date.today() - record.date_of_birth).days / 365.25
            else:
                record.age = 0

    def compute_last_visit_state(self):
        for record in self:
            patient_visit_id = record.env['hr_hospital.patient_visit'].search(
                [('patient_id', '=', record.id)], limit=1, order='visit_planned_datetime desc')
            record.last_visit_state = patient_visit_id.visit_status

    def open_patient_visit_act_window(self):
        """necessary method for hospital"""
        action = self.env['ir.actions.act_window']._for_xml_id('hr_hospital.patient_visit_act_window')
        action['domain'] = [('patient_id', '=', self.id)]
        return action

    def open_patient_visit_act_window_calendar(self):
        """necessary method for hospital"""
        action = {
            'name': 'Patient Visit',
            'type': 'ir.actions.act_window',
            'res_model': 'hr_hospital.patient_visit',
            'domain': [('doctor_id', '=', self.personal_doctor_id.id)],
            'context': {
                'default_doctor_id': self.personal_doctor_id.id,
                'default_patient_id': self.id,
            },
            'view_mode': 'calendar',
            'view_id': self.env.ref('hr_hospital.patient_visit_calendar').id,
        }
        return action
