#!/usr/bin/python3
"""
Python script that, using a REST API, fetches and
records TODO list progress for all employees.
"""

import requests
import json
import os


def get_employee_todo_progress(employee_id):
    """
    Fetch and record an employee's TODO list progress to a dictionary.

    Args:
        employee_id (int): The ID of the employee whose progress
        should be recorded.

    Returns:
        dict: A dictionary containing the progress information
        for the employee.
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

    # Record completed tasks for this employee
    completed_tasks = [
        {"username": employee_name, "task": task["title"],
         "completed": task["completed"]}
        for task in todo_data
    ]

    return completed_tasks


def main():
    all_employee_data = {}

    # Fetch and record TODO list progress for all employees
    # (user IDs from 1 to 10)
    for employee_id in range(1, 11):
        employee_progress = get_employee_todo_progress(employee_id)
        all_employee_data[str(employee_id)] = employee_progress

    # Export data to JSON
    output_file = "todo_all_employees.json"
    with open(output_file, "w") as json_file:
        json.dump(all_employee_data, json_file, indent=4)

    print(f"Data exported to {output_file}")


if __name__ == "__main__":
    main()
