#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting to CSV"""

import requests
import sys
import csv

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)

    csv_file_name = f"{employeeId}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in done_tasks:
            csv_writer.writerow([employeeId, employeeName, "Completed", task.get('title')])

    print(f"Data exported to {csv_file_name}")
