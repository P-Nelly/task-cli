# Task Manager

A Python-based command-line task management system that helps you organize and track tasks. Tasks are stored in a JSON file and can be easily managed through various commands.

## Features

- **Task Creation & Management**: Create, update, and delete tasks
- **Status Tracking**: Mark tasks as todo, in-progress, or done
- **Persistent Storage**: All tasks are stored in a JSON file
- **Filtering**: List tasks by status
- **Command-line Interface**: Easy to use CLI with intuitive commands

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-manager.git
   cd task-manager
   ```

2. Ensure you have Python 3.x installed:
   ```bash
   python --version
   ```

3. No additional dependencies required - uses Python standard library

## Usage

The task manager supports the following commands:

### Add a new task
```bash
python main.py add "Task description"
```

### Update a task
```bash
python main.py update <task_id> "New description"
```

### Delete a task
```bash
python main.py delete <task_id>
```

### Mark task status
```bash
python main.py mark-in-progress <task_id>
python main.py mark-done <task_id>
```

### List tasks
```bash
python main.py list              # List all tasks
python main.py list todo        # List only todo tasks
python main.py list in-progress # List only in-progress tasks
python main.py list done        # List only completed tasks
```

## Task Structure

Each task contains the following information:
- **ID**: Unique identifier
- **Description**: Task details
- **Status**: todo/in-progress/done
- **Created At**: Timestamp of creation
- **Updated At**: Timestamp of last update

## Data Storage

Tasks are stored in a `tasks.json` file in the project directory. The file is automatically created when you add your first task.

Example of stored task format:
```json
{
    "id": 1,
    "description": "Complete project documentation",
    "status": "in-progress",
    "createdAt": "2023-07-20T14:30:00",
    "updatedAt": "2023-07-20T15:45:00"
}
```

## Error Handling

The application includes basic error handling for:
- File operations
- JSON parsing
- Invalid command inputs
- Non-existent task IDs
- Invalid status values

## Development

### Project Structure
```
task-manager/
├── main.py
├── tasks.json
└── README.md
```

### Adding New Features
To contribute new features:
1. Fork the repository
2. Create a new branch for your feature
3. Implement your changes
4. Submit a pull request

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2023 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
```

This completes the README with all necessary sections, including detailed installation instructions, usage examples, project structure, contribution guidelines, and a license. The documentation is comprehensive and should give users all the information they need to use and contribute to the project.