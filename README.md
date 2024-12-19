<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">TASK-CLI</h1></p>
<p align="center">
    <em><code>A Python-based command-line task management system that helps you organize and track tasks</code></em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/license/p-nelly/task-cli?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
    <img src="https://img.shields.io/github/last-commit/p-nelly/task-cli?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/p-nelly/task-cli?style=default&color=0080ff" alt="repo-top-language">
</p>

<br>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Task-CLI is a command-line interface tool for managing tasks efficiently. Tasks are stored in a JSON file and can be easily managed through various commands. The application provides a simple yet powerful way to track your tasks' status and progress.

---

## Features

- **Task Creation & Management**: Create, update, and delete tasks
- **Status Tracking**: Mark tasks as todo, in-progress, or done
- **Persistent Storage**: All tasks are stored in a JSON file
- **Filtering**: List tasks by status
- **Command-line Interface**: Easy to use CLI with intuitive commands

---

## Project Structure

```
task-manager/
├── main.py
├── tasks.json
├── README.md
└── LICENSE
```

### Project Index
<details open>
    <summary><b><code>TASK-CLI/</code></b></summary>
    <details>
        <summary><b>__root__</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b>main.py</b></td>
                <td>Core application logic for task management</td>
            </tr>
            <tr>
                <td><b>tasks.json</b></td>
                <td>JSON storage for task data</td>
            </tr>
            </table>
        </blockquote>
    </details>
</details>

---

## Getting Started

### Prerequisites

- Python 3.x installed
- No additional dependencies required - uses Python standard library

### Installation

1. Clone the repository:
```sh
❯ git clone https://github.com/p-nelly/task-cli.git
```

2. Navigate to the project directory:
```sh
❯ cd task-cli
```

### Usage

The task manager supports the following commands:

**Add a new task:**
```sh
❯ python main.py add "Task description"
```

**Update a task:**
```sh
❯ python main.py update <task_id> "New description"
```

**Delete a task:**
```sh
❯ python main.py delete <task_id>
```

**Mark task status:**
```sh
❯ python main.py mark-in-progress <task_id>
❯ python main.py mark-done <task_id>
```

**List tasks:**
```sh
❯ python main.py list              # List all tasks
❯ python main.py list todo        # List only todo tasks
❯ python main.py list in-progress # List only in-progress tasks
❯ python main.py list done        # List only completed tasks
```

---

## Contributing

- [Join the Discussions](https://github.com/p-nelly/task-cli/discussions): Share your insights, provide feedback, or ask questions.
- [Report Issues](https://github.com/p-nelly/task-cli/issues): Submit bugs found or log feature requests.
- [Submit Pull Requests](https://github.com/p-nelly/task-cli/pulls): Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine.
3. **Create a New Branch**: Always work on a new branch.
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
6. **Push to GitHub**: Push the changes to your forked repository.
7. **Submit a Pull Request**: Create a PR against the original project repository.

</details>

---

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](LICENSE) file.

---

## Roadmap.sh project

This project was created for roadmap.sh

https://roadmap.sh/projects/task-tracker

---
