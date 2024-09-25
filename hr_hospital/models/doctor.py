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
