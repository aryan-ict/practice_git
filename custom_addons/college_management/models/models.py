# -*- coding: utf-8 -*-

from odoo import models, fields, api

'''
Creating a class with name college_management.
Using models.Model giving the type of model.
Assigning name for the model which is college_management.college_management.
Description is about describing the model is about College Management.
'''


class college_management(models.Model):
    _name = "college_management.college_management"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    '''Inherited models from base addons'''

    _description = "College Management"

    '''Assigning different fields with different fields type.'''
    name = fields.Char(string="Name")
    value = fields.Integer(string="Sr. Number")
    description = fields.Text()
    select_type = fields.Selection([('option1', 'Graduation'), ('option2', 'Post Graduation')], string="Degree Type")
    dob = fields.Date(string="Date Of Birth")
    status = fields.Selection(
        [('draft', 'Draft'), ('process', 'In Process'), ('confirm', 'Confirm'), ('cancelled', 'Cancelled')],
        default='draft', string="Status")

    def sample_button_d(self):
        print("Sample Button")
    '''Simple function for creation of button which prints 'Sample Button' on the click of the button'''
