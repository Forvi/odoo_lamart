import requests
from requests.auth import HTTPBasicAuth
import json


class JiraService:

    JIRA_URL = 'https://nforvi.atlassian.net/rest/agile/1.0/board'  # Замените на  URL Jira
    USERNAME = 'nforvi@mail.ru'  # Замените на  email
    API_TOKEN = 'ATATT3xFfGF0bcJ1b43-ktl1j1xZk-oPqBpUVZ7S5IsEeV_yh8paP7rmyG5-AcaJpOoR_kKDK8S8YcZ_xqW9RnCaQVGm6tEB-fmOXwdHSXZigrYOOKtHBIL3dnbMz5oE33HIg64xVfKRqmbSmX-u55HeLK3HHPcGWJ0ahPWJKDz28L3D1WN5K-4=358E948E'  # Замените на API токен

    @staticmethod
    def get_tasks(self):
        auth = HTTPBasicAuth(self.USERNAME, self.API_TOKEN)

        headers = {
            "Accept": "application/json"
        }

        response = requests.request(
            "GET",
            self.JIRA_URL,
            headers=headers,
            auth=auth
        )

        # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
        return json.dumps(json.loads(response.text))
