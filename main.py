import json
from typing import Any
import os
from datetime import datetime
import argparse


TASKS_FILE = "tasks.json"


def load_tasks() -> list[dict[str, Any]]:
    """
    Load tasks from a JSON file and return them
    :return: list[dict]
    """
    if not os.path.exists(TASKS_FILE):
        return []
    else:
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            print('Failed to load JSON')
            return []

def save_tasks(tasks: list[dict[str, Any]]) -> None:
    """
    Save tasks to JSON file
    :params: tasks: list[dict[str, Any]]
    :return: None
    """
    with open(TASKS_FILE, 'w',) as f:
        json.dump(tasks, f, indent=4)


def create_task(task_id: int, description: str) -> dict:
    """
    Create a task and return it
    :params: task_id: int, description: str
    :return: dict
    """
    return {
            'id': task_id,
            'description': description,
            'status': 'todo',
            'createdAt': datetime.now().isoformat(),
            'updatedAt': datetime.now().isoformat(),
    }


def update_task(tasks: list[dict[str, Any]], task_id: int, new_description: str) -> list[dict[str, Any]]:
    """
    Change the description of a task ( task_id ) to ( new_description )
    Then return updated tasks ( tasks )
    :params:
    :return:
    """
    return [
        {**task, 'description': new_description, 'updatedAt': datetime.now().isoformat()}
        if task['id'] == task_id
        else task
        for task in tasks
    ]


def delete_task(tasks: list[dict[str, Any]], task_id: int) -> list[dict[str, Any]]:
    """
    Delete a task with ID task_id from tasks
    Then return the updated tasks
    """
    return [task for task in tasks if task['id'] != task_id]

def update_status(tasks: list[dict[str, Any]], task_id: int, status: str) -> list[dict[str, Any]]:
    """
    Change of the task in tasks with the ID task_id to status 
    Then return the updated tasks
    """
    return [
        {**task, 'status': status, 'updatedAt': datetime.now().isoformat()}
        if task['id'] == task_id
        else task
        for task in tasks
    ]

def list_tasks(tasks: list[dict[str, Any]], status=None) -> None:
    """
    Print tasks tasks with status status to the console
    Or all if status undifined or ""
    """
    if status == '':
        status = None
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, CreatedAt: {task['createdAt']}, UpdatedAt: {task['updatedAt']}")


def get_id(tasks: list[dict[str, Any]]) -> int:
    """
    Find the lowest unused ID in tasks
    Then return it
    """
    used_ids = {t['id'] for t in tasks}

    current_id = 1

    while current_id in used_ids:
        current_id += 1

    return current_id

def main() -> None:

    # Create parsers and sub parsers to handle cli arguments
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

    # Handle arg parser input
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
        list_tasks(tasks, args.status)

if __name__ == "__main__":
    main()
