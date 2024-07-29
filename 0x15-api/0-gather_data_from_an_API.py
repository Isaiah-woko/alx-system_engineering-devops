#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
  returns information about his/her TODO list progress
"""

import requests
import sys
import re

REST_API_URL = "https://jsonplaceholder.typicode.com"


def todo_list_progress(employee_ID):
    """getting the todolist"""

    user_url = f'{REST_API_URL}/users/{employee_id}'
    todo_url = f'{REST_API_URL}/todos?userId={employee_id}'

    # Get reponses
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        return None

    user_data = user_response.json()
    employee_name = user_data['name']

    todos = todo_response.json()
    total_tasks = len(todos)
    done_tasks = [todo_task for todo_task in todos if todo_task['completed']]
    number_of_done_tasks = len(done_tasks)

    # display result
    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name, number_of_done_tasks, total_tasks))

    # Display the titles of completed tasks
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    if not re.fullmatch(r'\d+', sys.argv[1]):
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list_progress(employee_id)
