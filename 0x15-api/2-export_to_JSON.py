#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress and exports
it to JSON format.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display an employee's progress on their TODO list from an API.

    Args:
        employee_id (int): The ID of the employee whose progress
        should be checked.

    Returns:
        None
    """
    # Fetch employee name
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee's TODO list
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todo_data = todo_response.json()

    # Calculate completed and total tasks
    completed_tasks = [task for task in todo_data if task["completed"]]
    total_tasks = len(todo_data)
    completed_task_cnt = len(completed_tasks)

    # Print employee TODO list progress
    print("Employee {} is done with tasks ({}/{}):".format(employee_name,
                                                           completed_task_cnt,
                                                           total_tasks))

    for task in completed_tasks:
        print(f"\t {task['title']}")

    # Export data to JSON
    export_to_json(employee_id, employee_name, completed_tasks)


def export_to_json(employee_id, employee_name, completed_tasks):
    """
    Export employee's TODO list data to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        completed_tasks (list): List of completed tasks.

    Returns:
        None
    """
    data = {
        "USER_ID": [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            }
            for task in completed_tasks
        ]
    }

    file_name = f"{employee_id}.json"

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
