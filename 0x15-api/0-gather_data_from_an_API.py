#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv


def TODO(user_id):
    """ for a given employee ID, returns
        information about his/her TODO list progress.

    Args:
        user_id (int): user id of the
        of to do list
    """
    url = 'https://jsonplaceholder.typicode.com'
    users_url = "{}/users/{}".format(url, user_id)
    EMPLOYEE_NAME = requests.get(users_url).json().get('name')
    all_tasks = requests.get(f'{url}/todos?userId={user_id}').json()
    completed = f'{url}/todos?userId={user_id}&completed=true'
    done_tasks = requests.get(completed).json()

    tasks_size = len(all_tasks)
    done_len = len(done_tasks)
    print(f"Employee {EMPLOYEE_NAME} is done with ({done_len}/{tasks_size}):")
    for task in done_tasks:
        TASK_TITLE = task.get('title')
        print("\t " + TASK_TITLE)


if __name__ == "__main__":
    TODO(argv[1])
