#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

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
    completed_task_count = len(completed_tasks)

    # Print employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          completed_task_count,
                                                          total_tasks))

    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
