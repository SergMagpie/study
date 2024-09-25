from odoo import fields, models


class DefinePersonalDoctorWizard(models.TransientModel):
    _name = "hr_hospital.define.personal.doctor.wizard"
    _description = "DefinePersonalDoctorWizard"

    patient_ids = fields.Many2many(
        comodel_name='hr_hospital.patient',
        relation="hr_hospital_define_personal_doctor_rel",
        string='Patients',
        default=lambda self: self.env.context.get('active_ids', []),
    )
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string='Doctor',
    )

    def define_personal_doctor(self):
        self.patient_ids.update({
            'personal_doctor_id': self.doctor_id.id,
        })
