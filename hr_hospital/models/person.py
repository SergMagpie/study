from odoo import fields, models, api


class Person(models.AbstractModel):
    _name = "hr_hospital.person"
    _description = "Person"

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Name",
    )

    name = fields.Char(
        related="partner_id.name",
        string="Name",
    )

    surname = fields.Char(
        string="Surname",
        compute="compute_surname_first_name",
        inverse="inverse_surname_first_name",
        store=True,
    )

    first_name = fields.Char(
        string="First Name",
        compute="compute_surname_first_name",
        inverse="inverse_surname_first_name",
        store=True,
    )

    phone = fields.Char(
        string="Phone",
    )

    photo = fields.Image(
        string="Photo",
    )

    sex = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("neuter", "Neuter"),
        ],
        string="Sex",
    )

    @api.depends("partner_id.name")
    def compute_surname_first_name(self):
        for record in self:
            list_of_values = record.name.split(' ')
            first_name = ''.join(list_of_values[:1])
            surname = ' '.join(list_of_values[1:])
            record.first_name = first_name
            record.surname = surname

    def inverse_surname_first_name(self):
        for record in self:
            record.partner_id.name = ' '.join([i for i in
                                               [record.first_name,
                                                record.surname] if i])
