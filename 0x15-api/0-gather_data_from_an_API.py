#!/usr/bin/python3
"""
Python script that uses a REST API to get data, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

def fetch_todo_list(employee_id):
    """API url"""
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError ("Employee ID should be an integer")
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    if response.status_code == 200:
        data = response.json()

        employee_task = [task for task in data if task["userID"] == employee_id]
        completed_task = [task for task in employee_task if task["completed"]]
        total_task = len(employee_task)  
    
        print(f"Employee {employee_id} is done with tasks({completed_task}/{total_task}):")
        for task in employee_task:
            if task["completed"]:
                print(f"\t {task['title']}")
    else:
        print(f"Error: API request failed with status code {response.status_code}")
