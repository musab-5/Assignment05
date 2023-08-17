class Task:
    def set_task_detail(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority
        self.completed = False

    def mark_as_complete(self):
        self.completed = True
        print(f"Task '{self.task_name}' marked as completed.")

    def display_task_info(self):
        print("ToDo List")
        print("----------")
        print(f"Task: {self.task_name}")
        print(f"Priority: {self.priority}")
        print("Status: " + ("Completed" if self.completed else "Not Completed"))


# Create an object of the Task class
task = Task()

# Set task details
task.set_task_detail("Complete Assignment", "High")

# Mark task as complete
task.mark_as_complete()

# Display task information
task.display_task_info()
