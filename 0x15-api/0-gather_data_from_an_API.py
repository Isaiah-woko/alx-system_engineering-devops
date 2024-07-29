#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
  returns information about his/her TODO list progress
"""

import requests
import sys


def todo_list_progress(employee_ID):
    """getting the todolist"""

    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    # Todo list
    todo_reponse = requests.get(todo_url)

    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo['completed']]
    number_of_done_tasks = len(done_tasks)

    # display result
    print(
        f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}): ")

    # Display the titles of completed tasks
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    todo_list_progress(employee_id)
