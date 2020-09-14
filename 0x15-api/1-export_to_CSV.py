#!/usr/bin/python3
""" Export to CSV """
import csv
import requests
from sys import argv


def export_to_csv(user_id):
    """script to export data in the CSV format.

    Args:
        user_id (int): user id for every post
    """
    url = 'https://jsonplaceholder.typicode.com'
    users_url = "{}/users/{}".format(url, user_id)
    username = requests.get(users_url).json().get('username')
    all_tasks = requests.get('{}/todos?userId={}'.format(url, user_id)).json()

    with open('{}.csv'.format(user_id), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in all_tasks:
            task_title = task.get('title')
            task_status = task.get('completed')
            writer.writerow([user_id, username, task_status, task_title])


if __name__ == "__main__":
    export_to_csv(argv[1])
