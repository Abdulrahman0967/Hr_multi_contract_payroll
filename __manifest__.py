# -*- coding: utf-8 -*-
{
    'name': 'HR Multi Contract Payroll',
    'version': '19.0.1.0.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Allow multiple active contracts for payroll calculation',
    'description': """
        This module overrides default Odoo constraints to allow multiple active contracts per employee
        and calculates payroll accordingly.
    """,
    'author': 'Abdulrahman',
    'depends': ['hr', 'hr_contract'],
    'data': [

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}