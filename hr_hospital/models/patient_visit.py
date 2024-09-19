from odoo import fields, models


class PatientVisit(models.Model):
    _name = "hr_hospital.patient_visit"
    _description = "Patient Visit"

    visit_date = fields.Date(
        string="Visit Date")
    doctor = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string="Doctor",
    )
    patient = fields.Many2one(
        comodel_name='hr_hospital.patient',
        string="Patient",
    )
    disease = fields.Many2one(
        comodel_name='hr_hospital.disease',
        string="Disease",
    )
