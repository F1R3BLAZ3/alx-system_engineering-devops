#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list for the user
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_list)
    done_tasks = sum(1 for task in todo_list if task.get("completed"))

    # Display progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todo_list:
        if task.get("completed"):
            print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
