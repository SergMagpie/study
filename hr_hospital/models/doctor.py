from odoo import fields, models


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
