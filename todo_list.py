import os
import json

TODO_FILE = 'todo_list.json'

def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE , 'r') as file:
            return json.load(file)
    return []
def save_todo_list(todo_list):
    with open(TODO_FILE, 'w') as file:
        json.dump(todo_list, file , indent=4)
def add_todo(todo_list):
    task = input("Enter the task: ")
    todo_list.append({'task': task, 'done': False})
    print(f"Task '{task}' added.")

def view_todos(todo_list):
    if not todo_list:
        print("No tasks.")
    else:
        for idx , todo in enumerate(todo_list , start = 1):
            status = '✔️' if todo['done'] else '❌'
            print(f"idx : {idx} - {todo['task']} - {status}")

def mark_todo_done(todo_list):
    if not todo_list:
        print("No tasks to mark as done.")
        return
    while True:
        view_todos(todo_list)
        try:
            todo_id = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= todo_id < len(todo_list):
                todo_list[todo_id]['done'] = True
                print(f"Task '{todo_list[todo_id]['task']}' marked as done.")
                break
            else:
                print("Invalid task number. Enter a valid number.")
        except ValueError:
            print("Invalid task number.")
def delete_todo(todo_list):
    if not todo_list:
        print("No tasks to delete.")
        return
    while True:
        view_todos(todo_list)
        try:
            todo_id = int(input("Enter the task number to delete: ")) - 1
            if 0 <= todo_id < len(todo_list):
                task = todo_list.pop(todo_id)
                print(f"Task '{task['task']}' deleted.")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid task number.Enter a valid number.")
def main():
    todo_list = load_todo_list()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_todo(todo_list)
        elif choice == '2':
            view_todos(todo_list)
        elif choice == '3':
            mark_todo_done(todo_list)
        elif choice == '4':
            delete_todo(todo_list)
        elif choice == '5':
            save_todo_list(todo_list)
            print("Saved todo list.Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()