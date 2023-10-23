#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting to CSV"""

import requests
import sys
import csv

if __name__ == '__main__':
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    # Fetch employee information
    response = requests.get(url)
    employee = response.json()
    employeeName = employee.get('name')
    userId = employee.get('id')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # Create a CSV file with the user ID as the filename
    filename = f"{userId}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        done_tasks = []

        for task in tasks:
            if task.get('completed'):
                done_tasks.append(task)
                # Write task details to CSV
                csv_writer.writerow([userId, employeeName, "Completed", task.get('title')])

    print(f"Data exported to {filename}")

