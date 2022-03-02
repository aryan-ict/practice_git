"""This module is For Practice"""
from odoo import models, fields


class CollegeManagement(models.Model):
    """This class is for fields and ORM methods"""
    _name = "college.management"
    '''Inherited models from base addons'''
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Model for College Management"
    name = fields.Char(string="Name")
    mobile_no = fields.Char(string="Mobile Number")
    description = fields.Text()
    select_type = fields.Selection([('option1', 'Graduation'),
                                    ('option2', 'Post Graduation')],
                                   string="Degree Type",
                                   tracking=True)
    dob = fields.Date(string="Date Of Birth")
    status = fields.Selection(
        [('draft', 'Draft'), ('process', 'In Process'),
         ('confirm', 'Confirm'), ('cancelled', 'Cancelled')],
        default='draft', string="Status", tracking=True)

    def sample_button_d(self):
        """Function for sample button
        unlinks record"""
        self.unlink()

    def create_button(self):
        """Function for create button
        creates new values
        :return: record"""
        vals1 = {'name': 'Kavish',
                 'value': '03'}
        return self.create(vals1)

    def write_button(self):
        """Function for write button
        writes new values
        :return: record"""
        vals = {'name': 'Aryan',
                'value': '02',
                'description': 'Odoo Trainee',
                'select_type': 'option1'
                }
        return self.write(vals)

    def unlink_button(self):
        """Function for unlink button
        unlinks the selected record
        :returns: None"""
        self.unlink()
