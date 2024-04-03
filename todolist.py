# Define an empty list to store tasks
tasks = []

# Function to display the menu
def display_menu():
    print("\nTODO LIST APP")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

# Function to add a task
def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{index}. {task['task']} - {status}")

# Function to mark a task as done
def mark_task_as_done():
    view_tasks()
    task_index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

# Function to remove a task
def remove_task():
    view_tasks()
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_as_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
