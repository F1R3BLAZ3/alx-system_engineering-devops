#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress and
exports it to a CSV file.
"""

import csv
import os
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

    # Fetch employee name and username
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    user_data = user_response.json()
    employee_name = user_data.get("name")  # User's name
    employee_username = user_data.get("username")  # User's username

    # Fetch employee's TODO list
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todo_data = todo_response.json()

    # Export data to CSV
    export_to_csv(employee_id, employee_username, todo_data)


def export_to_csv(employee_id, employee_username, todo_data):
    """
    Export employee's TODO list data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        employee_username (str): The username of the employee.
        todo_data (list): List of employee's TODO tasks.

    Returns:
        None
    """
    file_name = f"{employee_id}.csv"
    file_path = os.path.join(os.getcwd(), file_name)

    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)

        for task in todo_data:
            csv_writer.writerow(
                [employee_id,
                 employee_username,
                 str(task["completed"]),
                 task["title"]])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
