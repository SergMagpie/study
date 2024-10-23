from odoo import fields, models, api
from odoo.tools.date_utils import start_of, end_of


class MonthDiseaseReportWizard(models.TransientModel):
    _name = "hr_hospital.month.disease.report.wizard"
    _description = "Month Disease Report Wizard"

    doctor_ids = fields.Many2many(
        comodel_name='hr_hospital.doctor',
        relation="disease_report_doctor_rel",
        string='Doctor',
        default=lambda self: self.env.context.get('active_ids', []),
    )
    disease_ids = fields.Many2many(
        comodel_name='hr_hospital.disease',
        relation="disease_report_disease_rel",
        string='Disease',
    )
    from_date = fields.Date(
        string='From Date',
        default=lambda self: start_of(fields.Date.today(), 'month'),
    )
    to_date = fields.Date(
        string='To Date',
        default=lambda self: end_of(fields.Date.today(), 'month'),
    )
    diagnosis_ids = fields.Many2many(
        comodel_name='hr_hospital.diagnosis',
        relation='disease_report_diagnosis_rel',
        string='Diagnosis',
    )

    @api.onchange('doctor_ids', 'disease_ids', 'from_date', 'to_date', 'diagnosis_ids')
    def onchange_for_diagnosis_ids(self):
        """necessary method for hospital"""
        search_domain = []
        if self.doctor_ids:
            patient_visit_ids = self.env['hr_hospital.patient_visit'].search([('doctor_id', 'in', self.doctor_ids.ids)])
            search_domain.append(('visit_id', 'in', patient_visit_ids.ids))
        if self.disease_ids:
            search_domain.append(('disease_id', 'in', self.disease_ids.ids))
        if self.from_date:
            patient_visit_ids = self.env['hr_hospital.patient_visit'].search(
                [('visit_real_datetime', '>=', self.from_date)])
            search_domain.append(('visit_id', 'in', patient_visit_ids.ids))
        if self.to_date:
            patient_visit_ids = self.env['hr_hospital.patient_visit'].search(
                [('visit_real_datetime', '<=', self.to_date)])
            search_domain.append(('visit_id', 'in', patient_visit_ids.ids))
        self.diagnosis_ids = [(6, 0, self.diagnosis_ids.search(search_domain).ids)]

    def month_disease_report(self):
        """necessary method for hospital"""
        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
            'lines': [{
                'visit_id': line.visit_id.name,
                'disease_id': line.disease_id.name,
                'description': line.description,
                'is_confirmed': 'confirmed' if line.is_confirmed else 'not confirmed',
            } for line in self.diagnosis_ids]
        }
        res = self.env.ref('hr_hospital.action_month_disease_report').report_action(self.diagnosis_ids.ids, data=data)
        return res
