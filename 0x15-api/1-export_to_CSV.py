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
    username = requests.get(users_url).json().get('name')
    all_tasks = requests.get(f'{url}/todos?userId={user_id}').json()

    with open('{}.csv'.format(user_id), 'w') as csv_file:
        for task in all_tasks:
            task_title = task.get('title')
            task_status = task.get('completed')
            fields = ['userId', 'name', 'completed', 'title']
            writer = csv.DictWriter(
                csv_file,
                fieldnames=fields,
                quoting=csv.QUOTE_ALL,
            )
            writer.writerow({
                'userId': user_id,
                'name': username,
                'completed': task_status,
                'title': task_title,
            })


if __name__ == "__main__":
    export_to_csv(argv[1])
