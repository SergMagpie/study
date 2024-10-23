from odoo.addons.hr_hospital.tests.common import HrHospitalGroupCommon
from odoo.tests import tagged, users
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install')
class TestAccessRights(HrHospitalGroupCommon):
    """My amazing test case."""

    @classmethod
    def setUpClass(cls):
        """Set up data for default group tests."""
        super(TestAccessRights, cls).setUpClass()

        cls.visit_1 = cls.env['hr_hospital.patient_visit'].create({
            'doctor_id': cls.doctor.id,
            'patient_id': cls.patient.id,
        })
        cls.visit_2 = cls.env['hr_hospital.patient_visit'].create({
            'doctor_id': cls.doctor_intern.id,
            'patient_id': cls.patient.id,
        })
        cls.visit_3 = cls.env['hr_hospital.patient_visit'].create({
            'doctor_id': cls.doctor.id,
            'patient_id': cls.patient_manager.id,
        })

    @users('patient_user')
    def test_access_patient_user(self):
        """just method for testing some test cases"""
        with self.assertRaises(AccessError):
            self.env['hr_hospital.patient_visit'].search([]).write({
                'description': 'description'
            })
        self.assertEqual(len(self.env['hr_hospital.patient_visit'].search([])),
                         2,
                         'Patient should see 2 visits')

    @users('intern_user')
    def test_access_intern_user(self):
        """just method for testing some test cases"""
        self.assertEqual(len(self.env['hr_hospital.patient_visit'].search([])),
                         1,
                         'Intern should see 1 visit')

    @users('manager_user')
    def test_access_manager_user(self):
        """just method for testing some test cases"""
        self.assertEqual(len(self.env['hr_hospital.patient_visit'].search(
            [('doctor_id', 'in', (self.doctor | self.doctor_intern).ids)])),
            3,
            'Manager should see 3 visit')

    @users('administrator_user')
    def test_access_administrator_user(self):
        """just method for testing some test cases"""
        self.assertEqual(len(self.env['hr_hospital.patient_visit'].search(
            [('doctor_id', 'in', (self.doctor | self.doctor_intern).ids)])),
            3,
            'Administrator should see 3 visit')
        self.visit_4 = self.env['hr_hospital.patient_visit'].create({
            'doctor_id': self.doctor.id,
            'patient_id': self.patient_manager.id,
        })
        self.assertEqual(len(self.env['hr_hospital.patient_visit'].search(
            [('doctor_id', 'in', (self.doctor | self.doctor_intern).ids)])),
            4,
            'Administrator should see 4 visit')
        self.env['hr_hospital.patient_visit'].search(
            [('doctor_id', 'in', (self.doctor | self.doctor_intern).ids)]).unlink()
        self.assertEqual(len(self.env['hr_hospital.patient_visit'].search(
            [('doctor_id', 'in', (self.doctor | self.doctor_intern).ids)])),
            0,
            "Administrator shouldn't see any visits")
