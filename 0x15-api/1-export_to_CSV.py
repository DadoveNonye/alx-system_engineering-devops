#!/usr/bin/python3
"""
export to csv file
"""

import csv
import requests
import sys


def fetch_todo_list(employee_id):
    """
    Fetches TODO list items for a given employee ID and 
    prints the completed tasks.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    if user_response.status_code == 200 and todo_response.status_code == 200:
        user_data = user_response.json()
        todo_data = todo_response.json()

        user_id = user_data.get("id")
        username = user_data.get("username")
        filename = f"{user_id}.csv"

        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for todo in todo_data:
                task_completed_status = "True" if todo.get("completed") else "False"
                task_title = todo.get("title")
                writer.writerow([user_id, username, task_completed_status, task_title])

        print(f"Data exported to {filename}")
    else:
        print(f"Error: API request failed with status codes {user_response.status_code}, {todo_response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list(employee_id)