from odoo import fields, models, api


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
    name = fields.Char(
        string="Diagnosis Name",
        related="disease_id.name",
    )
    visit_real_datetime = fields.Datetime(
        string="Date and time when the visit took place",
        compute='_compute_visit_real_datetime',
        store=True,
    )
    disease_type_id = fields.Many2one(
        comodel_name='hr_hospital.disease',
        string="Disease type",
        compute='_compute_disease_type',
        store=True,
    )

    @api.depends('disease_id')
    def _compute_disease_type(self):
        for record in self:
            record.disease_type_id = record.disease_id.parent_id.id or record.disease_id.id

    @api.depends('visit_id.visit_real_datetime')
    def _compute_visit_real_datetime(self):
        for record in self:
            record.visit_real_datetime = record.visit_id.visit_real_datetime
