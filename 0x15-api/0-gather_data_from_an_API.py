#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/'
    emp_url = url + employee_id
    todo_url = emp_url + "/todos"

    emp_res = requests.get(emp_url).json()
    todo_res = requests.get(todo_url).json()
    empl_name = emp_res.get('name')
    total = len(todo_res)
    done = 0
    for i in todo_res:
        if i.get("completed"):
            done += 1
    print("Employee {} is done with tasks({}/{}):".format(
                                    emp_name, done, total))
    for todo in todo_res:
        if todo.get("complicated"):
            tittle = todo.get('title')
            print("\t_{}".format(title))
