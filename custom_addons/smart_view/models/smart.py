"""This module is for Smart View Tasks"""
from odoo import models, fields
# from odoo.exceptions import ValidationError


class SmartView(models.Model):
    """This Class is for fields and ORM Functions"""
    _name = "smart.view"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Model for Smart View"
    name = fields.Char(string="Name")
    phone_no = fields.Char(string="Phone Number",
                           related='names_list.mobile_no')
    doc = fields.Datetime(string="Date Of Creation",
                          default=fields.Datetime.now)
    gender_id = fields.Selection([('male', 'Male'),
                                  ('female', 'Female'),
                                  ('transgender', 'Transgender')],
                                 string="Gender", tracking=True)
    status_bar = fields.Selection([('apply', 'Applied'),
                                   ('wait', 'Waiting'),
                                   ('approve', 'Approved')],
                                  default="apply",
                                  tracking=True)
    names_list = fields.Many2one('college.management',
                                 string="Name List")
    first_page = fields.One2many('smart.view.otm', 'appointment_id',
                                        string='Appointment Lines')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name is already in the database.")
    ]

    def smart_button(self):
        """This function is for smart button"""
        return self

    def log_button(self):
        """This function is for log button
        and posts a message in chatter on the click
        of the button and updates values.
        """
        up_vals = {'phone_no': '7575076690',
                   'gender_id': 'male'}
        self.message_post(body="Phone number has been updated "
                               "and Gender has been changed")
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


class SmartViewOtm(models.Model):
    """This class is for One2many field"""
    _name = "smart.view.otm"
    _description = "Smart View One2many"
    _rec_name = 'test_list'
    product_id = fields.Many2one('product.product', string='Product')
    product_qty = fields.Integer(string='Product Quantity')
    appointment_id = fields.Many2one('smart.view', string='Appointment ID')
    test_list = fields.Many2one('smart.view.otm', string='Test')
