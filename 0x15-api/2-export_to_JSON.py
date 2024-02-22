#!/usr/bin/python3

"""Export to json"""
import json
import requests


def export_todo_list_to_json(employee_id):
    """
    Fetches TODO list items for a given employee ID, generates a JSON object with
    user information and completed tasks, and saves it as USER_ID.json.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """

    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()

    # Check for successful user data retrieval
    if user_response.status_code != 200:
        print(f"Error: Failed to retrieve data {user_response.status_code}")
        return

    # Fetch TODO list items and filter user tasks
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_data = todo_response.json()

    if todo_response.status_code != 200:
        print(f"Error: Failed to retrieve list {todo_response.status_code}")
        return

    # Extract user information
    username = user_data.get("username")

    # Extract and format completed tasks
    completed_tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        for task in todo_data
        if task.get("completed")
    ]

    # Create the JSON data structure
    json_data = {
        "USER_ID": employee_id,
        "username": username,
        "tasks": completed_tasks,
    }

    # Save the JSON data to a file named USER_ID.json
    filename = f"{employee_id}.json"
    with open(filename, "w") as outfile:
        json.dump(json_data, outfile, indent=4)

    print(f"Employee TODO list exported successfully to {filename}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        if employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer.")
        export_todo_list_to_json(employee_id)
    except ValueError as e:
        print(f"Invalid employee ID: {e}")
