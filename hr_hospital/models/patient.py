from odoo import fields, models


class Patient(models.Model):
    _name = "patient"
    _description = "Patient"

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Name",
    )

    name = fields.Char(
        related="partner_id.name",
        string="Name",
    )
