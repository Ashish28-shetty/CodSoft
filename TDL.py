# Simple To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks):
            status = "✔" if task["done"] else "✘"
            print(f"{i+1}. {task['title']} [{status}]")

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task: ")
        tasks.append({"title": title, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Enter task number to update: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["title"] = input("Enter new task name: ")
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        show_tasks()
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        show_tasks()
        num = int(input("Enter task number to mark completed: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "6":
        print("Exiting application...")
        break

    else:
        print("Invalid choice. Try again.")