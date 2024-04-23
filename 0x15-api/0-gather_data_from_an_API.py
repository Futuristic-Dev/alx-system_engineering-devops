#!/usr/bin/python3

"""
Script that returns information about an employee's TODO list progress\n

Using a REST API.
"""


import requests
import sys


def get_employee_todo_progress(employee_id):
    """Retrieve and display the TODO list progress for employee."""
    base_url = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(task.get("completed", False) for task in todos_data)

    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, complete_tasks, total_tasks, end='\n'))

    for tasks in todos_data:
        if task.get('completed', False):
            print("\t {}".format(task.get("title")))


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
