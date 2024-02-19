#!/usr/bin/python3
"""Python script that fetches information about a given employee ID
using REST API, and returns information about his/her TODO list progress
in CSV format"""
import requests
import csv
import sys


def export_employee_todo_to_csv(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()
    name = user_data['username']

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([employee_id, name,
                                 task.get("completed"), task.get("title")])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_employee_todo_to_csv(employee_id)
