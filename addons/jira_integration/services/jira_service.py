import requests
from requests.auth import HTTPBasicAuth

# Параметры
JIRA_URL = 'https://nforvi.atlassian.net'  # Замените на  URL Jira
USERNAME = 'nforvi@mail.ru'  # Замените на  email
API_TOKEN = 'ATATT3xFfGF0PQywH7U-RO06MfEbaSgHNiKnQTt97NJOLNk8gsUc7c-E55WRi9Ph9YCbCaFCE7O4g2HevlokJ_NMGYauk98sA9BOjCpDZ23MyBDo8f9BtZHlBjDf_iOBL0uq38GwGiutCE0emv-lzbY-tH5uJWmhb5EffAax91AMi4gvTXwd-ZU=C4FE3D9F'  # Замените на API токен


class JiraService:
    @staticmethod
    def get_user_account_id(self, email):
        # URL для получения информации о пользователе
        url = f"{JIRA_URL}/rest/api/3/user/search?username={email}"

        # Выполнение GET-запроса
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, API_TOKEN))

        # Проверка статуса ответа
        if response.status_code == 200:
            users = response.json()
            if users:
                return users[0]['accountId']  # Возвращаем первый найденный accountId
            else:
                print("Пользователь не найден.")
                return None
        else:
            print(f"Ошибка: {response.status_code} - {response.text}")
            return None
    @staticmethod
    def get_user_teams(user_account_id):
        # URL для получения команд пользователя
        url = f"{JIRA_URL}/rest/tempo-teams/1/team?accountId={user_account_id}"

        # Выполнение GET-запроса
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, API_TOKEN))
        # Проверка статуса ответа
        if response.status_code == 200:
            teams = response.json()
            return teams
        else:
            print(f"Ошибка: {response.status_code} - {response.text}")
            return None

