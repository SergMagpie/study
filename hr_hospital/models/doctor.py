from odoo import fields, models, api


class Doctor(models.Model):
    _name = "hr_hospital.doctor"
    _description = "Doctor"
    _inherit = "hr_hospital.person"

    is_attending_physician = fields.Boolean(
        string="Is The Attending Physician",
    )
    specialty_id = fields.Many2one(
        comodel_name='hr_hospital.specialty',
        string="Specialty",
    )
    is_intern = fields.Boolean(
        string="Intern",
    )
    mentor_doctor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string="Mentor Doctor",
    )
    intern_ids = fields.One2many(
        comodel_name='hr_hospital.doctor',
        string="Intern",
        inverse_name='mentor_doctor_id',
    )
    intern_ids_char = fields.Char(
        compute='compute_intern_ids_char',
    )
    color = fields.Integer('Color Index', default=0)
    patient_visit_ids = fields.One2many(
        comodel_name='hr_hospital.patient_visit',
        string="Patient Visit",
        inverse_name='doctor_id',
    )
    patient_ids = fields.Many2many(
        comodel_name='hr_hospital.patient',
        string="Patients",
        compute='compute_patient_ids',
    )

    def open_patient_visit_act_window_calendar(self):
        """necessary method for hospital"""
        action = {
            'name': 'Patient Visit',
            'type': 'ir.actions.act_window',
            'res_model': 'hr_hospital.patient_visit',
            'domain': [('doctor_id', '=', self.id)],
            'context': {
                'default_doctor_id': self.id,
            },
            'view_mode': 'calendar',
            'view_id': self.env.ref('hr_hospital.patient_visit_calendar').id,
        }
        return action

    @api.depends('intern_ids')
    def compute_intern_ids_char(self):
        for record in self:
            record.intern_ids_char = ', '.join(record.intern_ids.mapped('name'))

    @api.depends('patient_visit_ids')
    def compute_patient_ids(self):
        for record in self:
            record.patient_ids = [(5, 0)] + [
                (4, patient_id.id) for patient_id in record.patient_visit_ids.mapped('patient_id')
            ]
