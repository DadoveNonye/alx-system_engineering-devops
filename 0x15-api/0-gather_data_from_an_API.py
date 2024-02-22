#!/usr/bin/python3
"""
Python script that uses a REST API to get data, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests


def fetch_todo_list(employee_id):
    """
    Fetches TODO list items for a given employee ID and prints the completed tasks.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    
    # Fetch TODO list items
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_data = todo_response.json()

    if user_response.status_code == 200 and todo_response.status_code == 200:
        
        employee_name = user_data.get("name")

        completed_tasks = [task.get("title")
                            for task in todo_data if task.get("completed")]

        total_tasks = len(todo_data)

        print(f"Employee {employee_name} is done with tasks 
              ({len(completed_tasks)}/{total_tasks}):")
        for task_title in completed_tasks:
            print(f"\t{task_title}")
    else:
        print(f"Error: API request failed with status codes
               {user_response.status_code}, {todo_response.status_code}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list(employee_id)
