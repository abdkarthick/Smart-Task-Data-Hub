import json
import os

def load_tasks():
    """
    Load tasks from the JSON file.
    Returns an empty list if file does not exist or is empty.
    """
    file_path = 'tasks.json'

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

def save_tasks(task_list):
    """
    Save the task list to the JSON file with proper formatting.
    """
    file_path = 'tasks.json'
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(task_list, file, indent=4, ensure_ascii=False)

def display_tasks(task_list):
    """
    Display all tasks with their completion status.
    """
    if not task_list:
        print("No tasks available at the moment.")
        return

    print("\n========== Your Task List ==========")
    for index, task_item in enumerate(task_list, start=1):
        status_symbol = "[Completed]" if task_item["completed"] else "[Pending]"
        print(f"{index}. {task_item['description']} - {status_symbol}")
    print("====================================\n")

def main():
    task_data = load_tasks()

    while True:
        print("\nTask Manager Menu")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Remove a task")
        print("5. Exit application")

        user_choice = input("Please enter your choice from 1 to 5: ").strip()

        if user_choice == "1":
            task_description = input("Enter the task description: ").strip()
            if task_description:
                task_data.append({"description": task_description, "completed": False})
                save_tasks(task_data)
                print("Task added successfully!")
            else:
                print("Task description cannot be empty. Please try again.")

        elif user_choice == "2":
            display_tasks(task_data)

        elif user_choice == "3":
            if not task_data:
                print("There are no tasks to mark as completed.")
                continue

            display_tasks(task_data)
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                task_index = task_number - 1

                if 0 <= task_index < len(task_data):
                    task_data[task_index]["completed"] = True
                    save_tasks(task_data)
                    print("Task marked as completed successfully!")
                else:
                    print("Invalid task number. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif user_choice == "4":
            if not task_data:
                print("There are no tasks to remove.")
                continue

            display_tasks(task_data)
            try:
                task_number = int(input("Enter the task number to remove: "))
                task_index = task_number - 1

                if 0 <= task_index < len(task_data):
                    removed_task = task_data.pop(task_index)
                    save_tasks(task_data)
                    print(f"Task '{removed_task['description']}' has been removed.")
                else:
                    print("Invalid task number. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif user_choice == "5":
            print("Thank you for using Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option between 1 and 5.")

if __name__ == "__main__":
    main()