#!/usr/bin/python3
"""Python script to export data in the json format."""

import json
import requests
import sys

REST_API_URL = "https://jsonplaceholder.typicode.com"


def todo_list_progress(employee_id):
    """getting the todolist"""

    user_url = f'{REST_API_URL}/users/{employee_id}'
    todo_url = f'{REST_API_URL}/todos?userId={employee_id}'

    # Get reponses
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)
    user_data = user_response.json()
    employee_name = user_data['username']
    todos = todo_response.json()

    dict_data = {employee_id: []}

    for todo_task in todos:
        completed_task = todo_task.get('completed')
        title = todo_task.get('title')
        data = {"task": title, "completed": completed_task,
                "username": employee_name}
        dict_data[employee_id].append(data)

    with open('{}.json'.format(employee_id), 'w') as file:
        json.dump(dict_data, file)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list_progress(employee_id)
