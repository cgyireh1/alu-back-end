#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export data to CSV
"""
import csv
import requests
from sys import argv


def to_csv():
    """Fetching API data."""
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

    """exportng to csv"""
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]

        """Creating a CSV writer object and writing each row to the CSV file"""
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in USER_TODO_DATA:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    to_csv()
