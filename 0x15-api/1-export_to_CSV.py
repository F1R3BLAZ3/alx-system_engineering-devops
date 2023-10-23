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

    # Fetch employee name
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    user_data = user_response.json()
    employee_name = user_data.get("username")

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

    # Export data to CSV
    export_to_csv(employee_id, employee_name, todo_data)


def export_to_csv(employee_id, employee_name, todo_data):
    """
    Export employee's TODO list data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todo_data (list): List of employee's TODO tasks.

    Returns:
        None
    """
    file_name = f"{employee_id}.csv"
    file_path = os.path.join(os.getcwd(), file_name)

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        # Write the header row
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                             "TASK_TITLE"])

        for task in todo_data:
            csv_writer.writerow((str(employee_id), employee_name,
                                 str(task["completed"]), task["title"]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
