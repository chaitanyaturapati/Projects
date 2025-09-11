tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append([task, False])
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for i in range(len(tasks)):
            status = "✅" if tasks[i][1] else "❌"
            print(f"{i + 1}. {tasks[i][0]} {status}")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1][1] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed[0]}' deleted successfully!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do List... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

main()
