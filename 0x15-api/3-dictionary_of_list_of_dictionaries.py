#!/usr/bin/python3
"""Python script that fetches all employees using REST API, and
returns information about his/her TODO list progress in JSON format"""
import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists for all employees."""
    base_url = "https://jsonplaceholder.typicode.com/"
    users_url = f'{base_url}users/'

    users_response = requests.get(users_url)
    users_data = users_response.json()

    all_user_data = {}
    for user in users_data:
        user_id = user["id"]
        user_url = f"{base_url}todos?userId={user_id}"
        todo_list = requests.get(user_url).json()

        all_user_data[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    return all_user_data


def export_to_json(data, filename="todo_all_employees.json"):
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    all_users = fetch_user_data()
    export_to_json(all_users)
