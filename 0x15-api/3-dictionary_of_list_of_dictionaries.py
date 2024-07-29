#!/usr/bin/python3
"""Python script to export data in the json format."""

import json
import requests

REST_API_URL = "https://jsonplaceholder.typicode.com"


def dict_employee_file():
    """Get employee and todo data from API."""
    users_url = f'{REST_API_URL}/users'
    users_response = requests.get(users_url)
    users_data = users_response.json()
    users_dict = {}
    filename = "todo_all_employees.json"

    for user in users_data:
        employee_id = user.get('id')
        username = user.get('username')
        todo_url = f"{REST_API_URL}/users/{employee_id}/todos"
        todo_response = requests.get(todo_url)
        tasks = todo_response.json()

        users_dict[employee_id] = []
        for task in tasks:
            completed = task.get('completed')
            title = task.get('title')
            task_dict = {
                "task": title,
                "completed": completed,
                "username": username
            }
            users_dict[employee_id].append(task_dict)

    with open(filename, mode='w') as file:
        json.dump(users_dict, file)


if __name__ == '__main__':
    dict_employee_file()
