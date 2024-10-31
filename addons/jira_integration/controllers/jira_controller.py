from odoo import http
from odoo.http import request, Response
from addons.jira_integration.services.jira_service import JiraService
import json


class JiraController(http.Controller):
    @http.route('/get_user_teams', auth='public', methods=['GET'], csrf=False)
    def get_user_teams(self, **kwargs):
        jira = JiraService()
        jira.

