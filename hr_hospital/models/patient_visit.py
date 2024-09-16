from odoo import fields, models


class PatientVisit(models.Model):
    _name = "patient.visit"
    _description = "Patient Visit"

    visit_date = fields.Date(
        string="Visit Date")
    doctor = fields.Many2one(
        comodel_name='doctor',
        string="Doctor",
    )
    patient = fields.Many2one(
        comodel_name='patient',
        string="Patient",
    )
    disease = fields.Many2one(
        comodel_name='disease',
        string="Disease",
    )
