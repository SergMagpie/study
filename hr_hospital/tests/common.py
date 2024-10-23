from odoo.tests import TransactionCase
from odoo.addons.base.tests.common import DISABLED_MAIL_CONTEXT


class HrHospitalGroupCommon(TransactionCase):
    """My amazing test case."""

    @classmethod
    def setUpClass(cls):
        """class method for setting up the test case"""
        super().setUpClass()

        cls.env = cls.env['base'].with_context(**DISABLED_MAIL_CONTEXT).env

        cls.group_patient = cls.env.ref('hr_hospital.group_hr_hospital_patient')
        cls.group_intern = cls.env.ref('hr_hospital.group_hr_hospital_intern')
        cls.group_doctor = cls.env.ref('hr_hospital.group_hr_hospital_doctor')
        cls.group_manager = cls.env.ref('hr_hospital.group_hr_hospital_manager')
        cls.group_administrator = cls.env.ref('hr_hospital.group_hr_hospital_administrator')

        cls.patient_user = cls.env['res.users'].create({
            'name': 'Test Patient',
            'login': 'patient_user',
            'password': 'patient_user',
            'email': 'patient_user@example.com',
            'groups_id': [(6, 0, cls.group_patient.ids)],
        })
        cls.intern_user = cls.env['res.users'].create({
            'name': 'Test Intern',
            'login': 'intern_user',
            'password': 'intern_user',
            'email': 'intern_user@example.com',
            'groups_id': [(6, 0, cls.group_intern.ids)],
        })
        cls.doctor_user = cls.env['res.users'].create({
            'name': 'Test Doctor',
            'login': 'doctor_user',
            'password': 'doctor_user',
            'email': 'doctor_user@example.com',
            'groups_id': [(6, 0, cls.group_doctor.ids)],
        })
        cls.manager_user = cls.env['res.users'].create({
            'name': 'Test Manager',
            'login': 'manager_user',
            'password': 'manager_user',
            'email': 'manager_user@example.com',
            'groups_id': [(6, 0, cls.group_manager.ids)],
        })
        cls.administrator_user = cls.env['res.users'].create({
            'name': 'Test Administrator',
            'login': 'administrator_user',
            'password': 'administrator_user',
            'email': 'administrator_user@example.com',
            'groups_id': [(6, 0, cls.group_administrator.ids)],
        })
        cls.doctor = cls.env['hr_hospital.doctor'].create({
            'partner_id': cls.doctor_user.partner_id.id,
        })
        cls.doctor_intern = cls.env['hr_hospital.doctor'].create({
            'partner_id': cls.intern_user.partner_id.id,
        })
        cls.patient = cls.env['hr_hospital.patient'].create({
            'partner_id': cls.patient_user.partner_id.id,
        })
        cls.patient_manager = cls.env['hr_hospital.patient'].create({
            'partner_id': cls.manager_user.partner_id.id,
        })
