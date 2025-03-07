# To-Do List CLI Application

This is a simple command-line interface (CLI) To-Do List application built with Python. It allows users to manage their tasks by adding, viewing, marking as completed, and deleting tasks. The tasks are stored in a JSON file for persistence.

## Features

- Add a new task
- View all tasks
- Mark a task as completed
- Delete a task
- Save tasks to a file
- Load tasks from a file

## Requirements

- Python 3.x

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todo_list.git
    cd todo_list
    ```

2. Create a virtual environment and activate it (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install any required dependencies (if any). For this simple project, there are no additional dependencies beyond standard Python libraries.

## Usage

1. Run the application:
    ```bash
    python todo_list.py
    ```

2. Follow the on-screen menu to manage your tasks:
    - Add task: Enter a new task to the list.
    - View tasks: Display all tasks with their status (completed or not).
    - Mark task as completed: Mark a task as completed based on its number.
    - Delete task: Delete a task from the list based on its number.
    - Exit: Save tasks to the file and exit the application.

## Example

```
To-Do List Menu:
1. Add task
2. View tasks
3. Mark task as completed
4. Delete task
5. Exit
Choose an option: 1
Enter the task: Buy groceries
Task 'Buy groceries' added.

To-Do List Menu:
1. Add task
2. View tasks
3. Mark task as completed
4. Delete task
5. Exit
Choose an option: 2
1. Buy groceries [❌]
```

## File Structure

```
todo_list/
├── todo_list.py
└── README.md
```

