# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime



class smart_view(models.Model):
    _name = "smart.view"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = "Model for Smart View"

    name = fields.Char(string="Name")
    phone_no = fields.Char(string="Phone Number", related='names_list.mobile_no')
    dob_id = fields.Datetime(string="Date Of Birth", default=fields.Datetime.now)
    gender_id = fields.Selection([('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')],
                                 string="Gender", tracking=True)
    status_bar = fields.Selection([('apply', 'Applied'), ('wait', 'Waiting'), ('approve', 'Approved')], default="apply",
                                  tracking=True)
    names_list = fields.Many2one('college.management', string="Name List")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name is already in the database."),
    ]

    def smart_button(self):
        print("hello")

    '''On the click of log button function will update the phone number and 
        change the gender and will enter a log note'''
    def log_button(self):
        up_vals = {'phone_no': '7575076690',
                   'gender_id': 'male'}
        self.message_post(body="Phone number has been updated and Gender has been changed")
        self.write(up_vals)

    # @api.constrains('name')
    # def check_name(self):
    #     for rec in self:
    #         if rec.name.isalpha() == False:
    #             raise ValidationError("Name must contain only alphabets")

    # @api.constrains('phone_no')
    # def check_number(self):
    #     for record in self:
    #         if len(record.phone_no) > 10 or len(record.phone_no) < 10:
    #             raise ValidationError("The number must be 10 digits long")
