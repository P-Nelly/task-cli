#TODO: Re-write functions based on function best practices
import json
import os
from datetime import datetime
import argparse


TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    else:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w',) as f:
        json.dump(tasks, f, indent=4)


def create_task(task_id, description):
    return {
            'id': task_id,
            'description': description,
            'status': 'todo',
            'createdAt': datetime.now().isoformat(),
            'updatedAt': datetime.now().isoformat(),
    }


def update_task(tasks, task_id, new_description):
    return [
        {**task, 'description': new_description, 'updatedAt': datetime.now().isoformat()}
        if task['id'] == task_id
        else task
        for task in tasks
    ]


def delete_task(tasks, task_id):
    return [task for task in tasks if task['id'] != task_id]

def update_status(tasks, task_id, status):
    return [
        {**task, 'status': status, 'updatedAt': datetime.now().isoformat()}
        if task['id'] != task_id
        else task
        for task in tasks
    ]

def list_tasks(tasks, status=None):
    if status == '':
        status = None
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, CreatedAt: {task['createdAt']}, UpdatedAt: {task['updatedAt']}")


def get_id(tasks):
    used_ids = {t['id'] for t in tasks}

    current_id = 1

    while current_id in used_ids:
        current_id += 1

    return current_id

def main():

    parser = argparse.ArgumentParser(description='Task Manager CLI')
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser('add', description='Add a new task')
    create_parser.add_argument('description', type=str, help='Description of the task')

    update_parser = subparsers.add_parser('update', description='Update a task')
    update_parser.add_argument('task_id', type=int, help='ID of task to update')
    update_parser.add_argument('new_description', help='New description for task')

    delete_parser = subparsers.add_parser('delete', description='Delete a task')
    delete_parser.add_argument('task_id', type=int, help='ID of task to delete')

    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', description='Mark a task as in progress')
    mark_in_progress_parser.add_argument('task_id', type=int, help='ID of task to mark as in progress')

    mark_done_parser = subparsers.add_parser('mark-done', description='Mark a task as done')
    mark_done_parser.add_argument('task_id', type=int, help='ID of task to mark done')

    list_parser = subparsers.add_parser('list', description='List all tasks or filter by status')
    list_parser.add_argument('status', nargs='?', choices=['todo', 'in-progress', 'done'], help='Status to filter list by')

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == 'add':
        save_tasks(tasks + [create_task(get_id(tasks), args.description)])

    if args.command == 'update':
        save_tasks(update_task(tasks, args.task_id, args.new_description))

    if args.command == 'delete':
        save_tasks(delete_task(tasks, args.task_id))

    if args.command == 'mark-in-progress':
        save_tasks(update_status(tasks, args.task_id, 'in-progress'))

    if args.command == 'mark-done':
        save_tasks(update_status(tasks, args.task_id, 'done'))

    if args.command == 'list':
        list_tasks(tasks, args.status) #TODO: Format table based on size of largest column item

if __name__ == "__main__":
    main()
