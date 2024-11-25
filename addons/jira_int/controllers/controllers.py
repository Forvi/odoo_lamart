# -*- coding: utf-8 -*-
from odoo import http
import requests
from requests.auth import HTTPBasicAuth
import json

from odoo.http import request

JIRA_URL = 'https://nforvi.atlassian.net/rest/agile/1.0/board'

USERNAME = 'nforvi@mail.ru'  # Замените на  email
API_TOKEN = ''

auth = HTTPBasicAuth(USERNAME, API_TOKEN)
headers = {
    "Accept": "application/json"
}

class JiraInt(http.Controller):
    @http.route('/jira_int/tasks', auth='public', website=True)
    def task(self, **kw):
        tasks = get_sprints()
        return http.request.render('jira_int.task', {
            'issues': tasks
        })


    @http.route('/jira_int/assigneetasks', auth='public', website=True)
    def assignee(self, **kw):
        name = 'Nikita Lavrov'
        assignee_tasks = get_issues_by_assignee(name)
        return http.request.render('jira_int.assignee', {
            'name': name,
            'assignee_tasks': assignee_tasks
        })


class Task:
    def __init__(self, status, story_point, name):
        self.status = status
        self.story_point = story_point
        self.name = name


class Sprint:
    def __init__(self, name_sprint, tasks):
        self.name_sprint = name_sprint
        self.tasks = tasks

class taskByAssigne:
    def __init__(self, key, assignee_task, story_point):
        self.key = key
        self.assignee_task = assignee_task
        self.story_point = story_point


def get_sprints():

    response = requests.request(
       "GET",
       JIRA_URL,
       headers=headers,
       auth=auth
    )

    sprints = response.json().get("values")
    list_task = []

    for sprint in sprints:

        name_sprint, tasks = get_tasks_on_sprint(sprint['id'])

        sprint = Sprint(name_sprint, tasks)
        list_task.append(sprint)

    return list_task


def get_tasks_on_sprint(id_board):
    JIRA_URL = f"https://nforvi.atlassian.net/rest/agile/1.0/board/{id_board}/issue?assignee={USERNAME}"
    response = requests.request(
        "GET",
        JIRA_URL,
        headers=headers,
        auth=auth
    )

    tasks = response.json().get("issues")
    name_sprint = tasks[0].get("fields").get("project").get("name")

    task_on_sprint = []
    for task in tasks:
        status = task.get("fields").get("status").get("name")
        story_point = task.get("fields").get("customfield_10016")
        name = task.get("fields").get("summary")
        new_task = Task(status, story_point, name)
        task_on_sprint.append(new_task)

    return name_sprint, task_on_sprint

def get_issues_by_assignee(assignee_name):
    JIRA_URL = f"https://nforvi.atlassian.net/rest/api/2/search?jql=assignee=\"{assignee_name}\""
    response = requests.get(JIRA_URL, headers=headers, auth=auth)

    if response.status_code == 200:
        issues = response.json().get("issues")
        result = []
        for issue in issues:
            issue_key = issue.get("key")
            assignee_name = issue.get('fields').get('summary')
            story_point = issue.get('fields').get('customfield_10016')
            tasks = taskByAssigne(issue_key, assignee_name, story_point)
            result.append(tasks)

        return result
    else:
        print(f"Ошибка: {response.status_code}")
        return None

    #
    # @http.route('/jira_int/jira_int/objects/<model("jira_int.jira_int"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('jira_int.object', {
    #         'object': obj
    #     })

