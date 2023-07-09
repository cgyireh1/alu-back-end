#!/usr/bin/python3


import requests
from sys import argv

def display():
    """Fetching API data"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
"""Iterating over the JSON response to find user with the specified id"""
for u in users.json():
        if u.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (u.get('name'))
            break
TOTAL_NUM_OF_TASKS = 0
NUMBER_OF_DONE_TASKS = 0
TASK_TITLE = []

