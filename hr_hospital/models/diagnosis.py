from odoo import fields, models


class Diagnosis(models.Model):
    _name = "hr_hospital.diagnosis"
    _description = "Diagnosis"
    _rec_name = "disease_id"

    visit_id = fields.Many2one(
        comodel_name='hr_hospital.patient_visit',
        string='Patient Visit',
    )
    disease_id = fields.Many2one(
        comodel_name='hr_hospital.disease',
        string="Disease",
    )
    description = fields.Char(
        string="Description",
        help="Purpose for treatment",
    )
    is_confirmed = fields.Boolean(
        string="Confirmed",
        help="This sign indicates that the given diagnosis, "
             "made by the mentor doctor, has been checked "
             "and approved by his mentor.",
    )
