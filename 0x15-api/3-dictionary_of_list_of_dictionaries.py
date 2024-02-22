#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json
import requests

def export_data():
    """
    Python script to export data in the JSON format.

    Args:
        USER_ID

    Returns:
        None
    """

    User_res = requests.get('https://jsonplaceholder.typicode.com/users')
    
    Task_res = requests.get("https://jsonplaceholder.typicode.com/todos")

    if User_res.status_code == 200 and Task_res.status_code == 200:
        users = User_res.json()
        tasks = Task_res.json()

        user_tasks = {}
        for user in users:
            user_id = user['id']
            user_name = user['username']
            user_tasks[user_id] = []

            for task in tasks:
                if task['userId'] == user_id:
                    user_tasks[user_id].append({
                        'username': user_name,
                        'task': task['title'],
                        'completed': task['completed']
                    })


        filename = 'todo_all_employees.json'
        with open(filename, "w") as json_file:
            json.dumps(json_data, json_file, indent=4)

if __name__ == '__main__':
    export_data()

