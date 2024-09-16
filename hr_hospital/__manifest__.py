{
    'name': 'HR Hospital',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': "Module for hospital automation: keeping records of doctors and patients.",
    'description': """
    This module for hospital automation: keeping records of doctors and patients.
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
    ],
    'demo': [
        'demo/doctor_demo_data.xml',
        'demo/patient_demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}
