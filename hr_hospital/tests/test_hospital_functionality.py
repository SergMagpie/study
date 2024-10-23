from datetime import datetime

from odoo.addons.hr_hospital.tests.common import HrHospitalGroupCommon
from odoo.tests import tagged
from odoo.exceptions import UserError


@tagged('post_install', '-at_install')
class TestHospitalFunctionality(HrHospitalGroupCommon):
    """My amazing test case."""

    @classmethod
    def setUpClass(cls):
        """class method for setting up the test case"""
        super(TestHospitalFunctionality, cls).setUpClass()
        cls.test_patient_visit = cls.env['hr_hospital.patient_visit'].create({
            'doctor_id': cls.doctor.id,
            'patient_id': cls.patient.id,
            'visit_planned_datetime': datetime.now(),
        })

    def test_compute_surname_first_name(self):
        """just method for testing some test cases"""
        self.assertEqual(self.doctor.name, 'Test Doctor')
        self.assertEqual(self.doctor.surname, 'Doctor')
        self.assertEqual(self.doctor.first_name, 'Test')
        self.doctor.partner_id.name = 'New Doctor'
        self.assertEqual(self.doctor.name, 'New Doctor')
        self.assertEqual(self.doctor.surname, 'Doctor')
        self.assertEqual(self.doctor.first_name, 'New')

    def test_inverse_surname_first_name(self):
        """just method for testing some test cases"""
        self.doctor.first_name = 'first_name'
        self.doctor.surname = 'surname'
        self.assertEqual(self.doctor.name, 'first_name surname')

    def test_patient_visit_defends(self):
        """just method for testing some test cases"""
        with self.assertRaises(UserError):
            self.test_patient_visit.write({
                'visit_status': 'completed',
            })

    def test_check_doctor_id(self):
        """just method for testing some test cases"""
        with self.assertRaises(UserError):
            self.test_patient_visit.create({
                'doctor_id': self.doctor.id,
                'patient_id': self.patient.id,
                'visit_planned_datetime': datetime.now(),
            })
