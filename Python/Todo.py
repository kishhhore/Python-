# todo_manager.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i + 1}. [{status}] {task['task']}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTODO LIST MANAGER")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Remove Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '3':
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
