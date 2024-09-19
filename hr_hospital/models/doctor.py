from odoo import fields, models


class Doctor(models.Model):
    _name = "hr_hospital.doctor"
    _description = "Doctor"

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Name",
    )

    name = fields.Char(
        related="partner_id.name",
        string="Name",
    )

    is_attending_physician = fields.Boolean(string="Is The Attending Physician")
