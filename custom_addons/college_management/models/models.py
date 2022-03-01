# -*- coding: utf-8 -*-

from odoo import models, fields, api

'''
Creating a class with name college_management.
Using models.Model giving the type of model.
Assigning name for the model which is college_management.college_management.
Description is about describing the model is about College Management.
'''


class college_management(models.Model):
    _name = "college.management"

    '''Inherited models from base addons'''
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = "Model for College Management"

    '''Assigning different fields with different fields type.'''
    name = fields.Char(string="Name")
    mobile_no = fields.Char(string="Mobile Number")
    description = fields.Text()
    select_type = fields.Selection([('option1', 'Graduation'), ('option2', 'Post Graduation')], string="Degree Type",
                                   tracking=True)
    dob = fields.Date(string="Date Of Birth")
    status = fields.Selection(
        [('draft', 'Draft'), ('process', 'In Process'), ('confirm', 'Confirm'), ('cancelled', 'Cancelled')],
        default='draft', string="Status", tracking=True)

    def sample_button_d(self):
        pass

    def create_button(self):
        vals1 = {'name': 'Kavish',
                 'value': '03'},
        return self.create(vals1)

    def write_button(self):
        vals = {'name': 'Aryan',
                'value': '02',
                'description': 'Odoo Trainee',
                'select_type': 'option1'
                }
        return self.write(vals)

    def unlink_button(self):
        self.unlink()
'''Simple function for creation of button which prints 'Sample Button' on the click of the button'''
