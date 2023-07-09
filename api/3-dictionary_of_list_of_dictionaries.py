#!/usr/bin/python3

"""
Request from API, Return TODO list progress of all employees &
Expo[[Ort data to JSON
"""
import json
import requests


def all_to_json():
    """Fetching API data."""
    USERS = []
    todoers = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in todoers.json():
        USERS.append((u.get('id'), u.get('username')))
    USER_TODO_DATA = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        USER_TODO_DATA.append((t.get('userId'),
            t.get('completed'),
            t.get('title')))

    """exporting to json"""
    data = dict()
    for u in USERS:
        t = []
        for task in USER_TODO_DATA:
            if task[0] == u[0]:
                t.append({"task": task[2], "completed": task[1],
                          "username": u[1]})
        """Addinglist of TODO items of current employee to the dictionary"""      
        data[str(u[0])] = t
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)


if __name__ == "__main__":
    all_to_json()
