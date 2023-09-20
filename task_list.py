class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def show_tasks(self):
        print("Task List:")
        for i, task in enumerate(self.tasks):
            status = "✓" if task.completed else "✗"
            print(f"{i+1}. [{status}] {task.description}")

if __name__ == "__main__":
    task_list = TaskList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task_list.add_task(description)

        elif choice == "2":
            index = int(input("Enter task index to complete: ")) - 1
            task_list.complete_task(index)

        elif choice == "3":
            task_list.show_tasks()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")