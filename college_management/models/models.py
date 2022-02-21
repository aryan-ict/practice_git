# -*- coding: utf-8 -*-

from odoo import models, fields, api


class college_management(models.Model):
    _name = "college_management.college_management"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "College Management"

    name = fields.Char()
    value = fields.Integer(string="Sr. Number")
    description = fields.Text()
    select_type = fields.Selection([('option1', 'Graduation'), ('option2', 'Post Graduation')], string="Degree Type")
    dob = fields.Date(string="Date Of Birth")
    status = fields.Selection(
        [('draft', 'Draft'), ('process', 'In Process'), ('confirm', 'Confirm'), ('cancelled', 'Cancelled')], default='draft', string="Status")


    def sample_button_d(self):
        print("Sample Button")

