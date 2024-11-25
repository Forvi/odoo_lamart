import requests
from requests.auth import HTTPBasicAuth

JIRA_URL = 'https://nforvi.atlassian.net/rest/agile/1.0/board'

USERNAME = 'nforvi@mail.ru'  # Замените на  email
API_TOKEN = 'ATATT3xFfGF0bcJ1b43-ktl1j1xZk-oPqBpUVZ7S5IsEeV_yh8paP7rmyG5-AcaJpOoR_kKDK8S8YcZ_xqW9RnCaQVGm6tEB-fmOXwdHSXZigrYOOKtHBIL3dnbMz5oE33HIg64xVfKRqmbSmX-u55HeLK3HHPcGWJ0ahPWJKDz28L3D1WN5K-4=358E948E'  # Замените на API токен

auth = HTTPBasicAuth(USERNAME, API_TOKEN)
headers = {
    "Accept": "application/json"
}


class Task:
    def __init__(self, status, story_point, name):
        self.status = status
        self.story_point = story_point
        self.name = name


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
        task = get_tasks_on_sprint(sprint['id'])
        list_task.append(task)
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

    task_on_sprint = []
    for task in tasks:
        status = task.get("fields").get("status").get("name")
        story_point = task.get("fields").get("customfield_10016")
        name = task.get("fields").get("project").get("name")
        new_task = Task(status, story_point, name)
        task_on_sprint.append(new_task)

    return task_on_sprint
