from odoo import fields, models


class Patient(models.Model):
    _name = "hr_hospital.patient"
    _description = "Patient"
    _inherit = "hr_hospital.person"

    personal_doctor_id = fields.Many2one(
        comodel_name="hr_hospital.doctor",
        string="Personal doctor",
    )

    date_of_birth = fields.Date(
        string="Date of Birth",
    )

    age = fields.Integer(
        string="Age",
        compute="compute_age",
    )

    passport_data = fields.Char(
        string="Passport data",
    )

    contact_person_id = fields.Many2one(
        comodel_name="res.partner",
        string="Contact Person",
    )

    def compute_age(self):
        for record in self:
            if record.date_of_birth:
                record.age = (fields.Date.today() - record.date_of_birth)
            else:
                record.age = 0
