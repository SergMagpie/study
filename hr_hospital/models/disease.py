from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class Disease(models.Model):
    _name = "hr_hospital.disease"
    _description = "Disease"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(
        string="Name",
        translate=True,
    )
    complete_name = fields.Char(
        string='Complete Name',
        compute='_compute_complete_name',
        recursive=True,
        store=True,
    )
    parent_id = fields.Many2one(
        comodel_name='hr_hospital.disease',
        string='Parent Category',
        index=True,
        ondelete='cascade',
    )
    child_id = fields.One2many(
        comodel_name='hr_hospital.disease',
        inverse_name='parent_id',
        string='Child Categories')
    parent_path = fields.Char(index=True, unaccent=False)

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        """necessary method for hospital"""
        for disease in self:
            if disease.parent_id:
                disease.complete_name = '%s / %s' % (disease.parent_id.complete_name, disease.name)
            else:
                disease.complete_name = disease.name

    @api.constrains('parent_id')
    def _check_disease_recursion(self):
        """necessary method for hospital"""
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive Disease.'))

    @api.model
    def name_create(self, name):
        """necessary method for hospital"""
        disease = self.create({'name': name})
        return disease.id, disease.display_name

    @api.depends_context('hierarchical_naming')
    def _compute_display_name(self):
        """necessary method for hospital"""
        if self.env.context.get('hierarchical_naming', True):
            return super()._compute_display_name()
        for record in self:
            record.display_name = record.name

    @api.ondelete(at_uninstall=False)
    def _unlink_except_default_category(self):
        """necessary method for hospital"""
        main_disease = self.env.ref('hr_hospital.disease_all', raise_if_not_found=False)
        if main_disease and main_disease in self:
            raise UserError(_("You cannot delete this disease, it is the default generic disease."))
