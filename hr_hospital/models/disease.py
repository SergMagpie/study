from odoo import fields, models


class Disease(models.Model):
    _name = "hr_hospital.disease"
    _description = "Disease"

    name = fields.Char(string="Name")
