{
    'name': 'HR Hospital',
    'version': '17.0.2.0.0',
    'category': 'Human Resources',
    'summary': "Module for hospital automation: keeping records of doctors and patients.",
    'description': """
    This module for hospital automation: keeping records of doctors and patients.
    17.0.2.0.0 - updated for module 3
    """,
    'depends': [
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/disease_data.xml',
        'views/menu.xml',
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/disease_view.xml',
        'views/patient_visit_view.xml',
        'views/diagnosis_view.xml',
        'views/specialty_view.xml',
        'views/disease_report_template.xml',
        'views/disease_report.xml',
        'wizard/define_personal_doctor_wizard.xml',
        'wizard/month_disease_report_wizard.xml',
    ],
    'demo': [
        'demo/doctor_demo_data.xml',
        'demo/patient_demo_data.xml',
        'demo/disease_demo_data.xml',
        'demo/patient_visit_demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}
