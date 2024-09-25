from odoo import fields, models


class Specialty(models.Model):
    _name = "hr_hospital.specialty"
    _description = "Specialty"

    name = fields.Char(
        string="Specialty",
    )
