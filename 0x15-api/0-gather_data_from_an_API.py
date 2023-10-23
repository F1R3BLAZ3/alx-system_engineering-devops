#!/usr/bin/python3
"""
Fetch and display an employee's progress on their TODO list from an API.
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
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{user_url}/todos'

    # Fetch user data
    user_data = requests.get(user_url).json()
    employee_name = user_data.get('name')

    # Fetch TODO list for the user
    todo_list = requests.get(todo_url).json()

    # Calculate progress
    total_tasks = len(todo_list)
    done_tasks = sum(1 for task in todo_list if not task.get('completed'))

    # Display progress
    print(f"Employee {employee_name} is done with tasks "
          f"({done_tasks}/{total_tasks}):")
    for task in todo_list:
        if not task.get('completed'):
            print(f'\t {task.get("title")}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    get_employee_todo_progress(employee_id)
