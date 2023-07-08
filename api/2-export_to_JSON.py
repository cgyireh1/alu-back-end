#!/usr/bin/python3


"""
Request from API; Return TODO list progress given employee ID
Export this data to JSON
"""
from sys import argv
import json
import requests


def to_json():
    """
    Fetching API data.
    """
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in users.json():
        if u.get('id') == int(argv[1]):
            USERNAME = (u.get('username'))
            break
    USER_TODO_DATA = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            USER_TODO_DATA.append((t.get('completed'), t.get('title')))

    """exporting to json file"""
    t = []
    for task in USER_TODO_DATA:
        t.append({"task": task[1], "completed": task[0], "username": USERNAME})
    data = {str(argv[1]): t}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    to_json()

