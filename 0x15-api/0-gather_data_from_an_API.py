#!/usr/bin/python3
"""Python script that fetches information about a given employee ID
using REST API, and returns information about his/her TODO list progress."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    completed = [task for task in todos_data
                 if task.get("completed") is True]
    all_tasks = len(todos_data)
    count = len(completed)
    name = user_data['name']

    print(f"Employee {name} is done with tasks({count}/{all_tasks}):")

    for task in completed:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
