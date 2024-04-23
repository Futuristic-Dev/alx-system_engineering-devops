#!/usr/bin/python3

"""
Extend Python script to export data in the CSV format.

Using the recent task.
Requirements:\n
    -Records all tasks that are owned by this employee
    -Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    -File name must be: USER_ID.csv
"""


import csv
import requests
import sys


def get_employee_info_and_tasks(employee_id):
    """
    Retrieve information about the employee and their tasks from.\n

    JSONPlaceholder API.
    """

    api_url = 'https://jsonplaceholder.typpicode.com/'

    user_url = '{}users/{}'.format(api_url, employee_id)
    todos_url = '{}todos?userId={}'.format(api_url, employee_id)

    user_response = requests.get(user_url)
    user_data = user_response.json()

    username = user_data.get('username')

    todos_response = requests.get(todos_url)
    tasks_data = todos_response.json()

    tasks_list = []
    for task in tasks_data:
        tasks_lists.append(
                [
                    employee_id, username, task.get('completed'), task.get('title')
                    ])
    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(
                employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks_list:
            employee_writer.writerow(task)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    get_employee_info_and_tasks(employee_id)
