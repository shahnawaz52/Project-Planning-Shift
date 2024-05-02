# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Project Planning Shift',
    'description':""" Create shift on creation of task
    Task Id = '2894390'
    """,
    'version' : '15.0.1.0.1',
    'author': 'Odoo PS',
    'category': 'Custom Development',
    'depends' : ['project_timesheet_forecast_sale'],
    'data': [
        'views/project_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
