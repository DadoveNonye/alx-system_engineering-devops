#!/usr/bin/python3
"""
Python script that uses a REST API to get data, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

def fetch_todo_list(employee_id):
    """API url"""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            todo_list = response.json()
            completed_task = [task['task'] for task in todo_list if task['completed']]

            total_task = len(todo_list)
            num_completed_task = len(completed_task)
            print(f"Employee {todo_list[0]['userId']} is done with tasks ({num_completed_tasks}/{total_tasks}):")
            for task_title in completed_tasks:
                print(f"\t{task_title}")
        else:
            print("failed to fetch TODO list")
    except Exception as e:
        print(f"error occured: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list(employee_id)
