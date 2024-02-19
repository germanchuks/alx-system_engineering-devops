#!/usr/bin/python3
"""Python script that fetches information about a given employee ID
using REST API, and returns information about his/her TODO list progress
in JSON format"""
import json
import requests
import sys


def export_employee_todo_to_json(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()
    name = user_data.get("username")

    json_filename = f"{employee_id}.json"
    json_data = {
        "USER_ID": [
            {"task": task.get("title"), "completed": task.get("completed"),
             "username": name}
            for task in todos_data
        ]
    }
    with open(json_filename, "w") as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_employee_todo_to_json(employee_id)
