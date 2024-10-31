from odoo import models, api, fields, models

class Task(models.Model):
    _name = 'jira.task'

    task_id = fields.Integer(string='Task ID')
    name = fields.Char(string='Project name')
    description = fields.Text(string='Description')
