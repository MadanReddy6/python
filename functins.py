from todo import Todo_Item, Todo_List
import os



def save_todo_list(todo_list):
    with open(f"./todo_data/{todo_list.owner.lower()}.txt","w") as f:
        lines = []

        for item in todo_list.todo_items:
            if item.priority:
                priority = item.priority
            else:
                priority = "None"

            if item.done:
                done = "True"
            else:
                done = "False"

            task = item.task.replace(","," ")

            line = ",".join([priority,done,task])
            lines.append(line)

        f.write("\n".join(lines))
            


print("Welcome to TODO APP")

while True:
    owner_name = input("Hello, Please enter your name:")
    if owner_name:
        break
    else:
        print("Owner Name cant be empty...")


# try to find the owner
PATH = f"./todo_data/{owner_name.lower()}.txt"
try:
    with open(PATH, "x") as f:
        print(f"Welcome {owner_name} to our TODO app")
        user_list = Todo_List(owner_name)
except:
    print(f"Welcome Back")

    with open(PATH, "r") as f:
        todo_data = f.readlines()
        todo_items = []
        for line in todo_data:
            line = line.replace("\n","")
            priority, done, task = line.split(",")

            if done == "True":
                done = True
            else:
                done = False

            if priority == "None":
                priority = None

            todo_item = Todo_Item(task, priority, done)
            todo_items.append(todo_item)

        user_list = Todo_List(owner_name, todo_items)


while True:
    print("""\n\nWhat do you want to do?
    
    1. Create a new task
    2. View existing task
    3. Mark a task as done
    4. Edit a old task 
    5. Delete a task
    6. Exit

    """)

    while True:
        choice = input("Enter a number (1-6) : ")

        try:
            choice = int(choice)
            if (choice >= 1) and (choice <=6):
                break
            else:
                print("Choice must be between 1-6 ")
        except:
            print("Choice must be a valid number")

    
    # quitting the app
    if choice == 6:
        # saving
        quit()

    # creating new todo item
    elif choice == 1:

        while True:
            task = input("\nTask: ")
            if task:
                break
            else:
                print("Task must not be empty!")

        while True:
            priority = input("\nPriority: ")

            if priority:
                priority = priority.lower().title()

                if priority in ["High", "Medium", "Low"]:
                    break
                else:
                    print("Priority must be one of",["High", "Medium", "Low"])
            else:
                priority = None
                break

        while True:
            done = input("\nDone? (y/N) :")

            if done:
                done = done.lower()
                if done in ["y", "yes"]:
                    done = True
                    break
                elif done in ["n", "no"]:
                    done = False
                    break
                else:
                    print("Done must be one of y / n")
            else:
                done = False
                break
        
        created_item = Todo_Item(task,priority,done)
        print("\nNew task created")
        print(created_item)

        user_list.add_todo_item(created_item)
        save_todo_list(user_list)
    # printing out all the todo items in the owner's todo list
    elif choice == 2:
        print(f"\n{user_list}")
    # option to mark task as done
    elif choice == 3:
        print(f"\n{user_list}")
        number = int(input("Enter your task number to mark done : "))
        user_list.finish_todo_item(number)
        save_todo_list(user_list)
    elif choice == 4:
        print(f"\n{user_list}")
        number = int(input("Enter your task number to edit: "))

        if number <= len(user_list.todo_items) and number > 0:
            todo_item = user_list.todo_items[number - 1]

            print(f"Editing task #{number}: {todo_item}")

            new_task = input("Enter new task : ")
            if new_task:
                todo_item.task = new_task

            new_priority = input("Enter new priority : ").lower().title()
            if new_priority in ["High", "Medium", "Low", "None"]:
                todo_item.priority = None if new_priority == "None" else new_priority

            new_done = input("Is the task done? (y/N): ").lower()
            if new_done in ["y", "yes"]:
                todo_item.done = True
            elif new_done in ["n", "no"]:
                todo_item.done = False

            print("\nTask updated")
            print(todo_item)

            save_todo_list(user_list)
        else:
            print("Invalid task number")
    elif choice == 5:
        print(f"\n{user_list}")
        number = int(input("Enter your task number to be deleted : "))
        user_list.delete_todo_item(number)
        save_todo_list(user_list)

    else:
        print(f"Choice : {choice}")




    class Todo_Item:
    priority_options = ["High", "Medium", "Low"]

    def _init_(self, task: str, priority: str = None, done: bool = False):
        if type(task) == str:
            if task:
                self.task = task
            else:
                raise Exception("Task should not be empty")
        else:
            raise Exception("Task needs to be a string")

        if type(done) == bool:
            self.done = done
        else:
            raise Exception("Done argument needs to be a boolean")

        if priority:
            if priority in Todo_Item.priority_options:
                self.priority = priority
            else:
                raise Exception(
                    f"priority setting should be one of {Todo_Item.priority_options}")
        else:
            self.priority = None

    def _str_(self):
        return f'[{"x" if self.done else "o"}] - {self.priority if self.priority else "None"} : {self.task}'

    def finish(self):
        self.done = True

    def raise_priority(self):
        if not self.priority:
            return

        if self.priority == "Low":
            self.priority = "Medium"
        if self.priority == "Medium":
            self.priority = "High"


class Todo_List:
    def _init_(self, owner: str, todo_list: list = []):

        for item in todo_list:
            if type(item) != Todo_Item:
                raise Exception(f"Expected Todo Item got {type(item)}")

        self.todo_items = todo_list

        if type(owner) == str:
            if owner:
                self.owner = owner
            else:
                raise Exception("Owner name should not be empty")
        else:
            raise Exception("Owner name needs to be a string")

    def _str_(self):
        # write code so the output is like the following
        output = f"{self.owner}'s ToDo List\n"

        for item in self.todo_items:
            output += str(item) + "\n"

        return output

    def info(self):
        pending_tasks = {"High": 0, "Medium": 0, "Low": 0}
        finished_tasks = 0

        for item in self.todo_items:
            if item.done:
                finished_tasks += 1
            else:
                if item.priority:
                    pending_tasks[item.priority] += 1

        pending_summary = ", ".join(
            [f"{priority} - {count}" for priority, count in pending_tasks.items()])

        print(f"{self.owner}'s Todo list\n\nPending Tasks: {len(self.todo_items) - finished_tasks} \n{pending_summary}\nFinished Tasks: {finished_tasks}\n------------")

    def add_todo_item(self, todo_item):
        if type(todo_item) == Todo_Item:
            self.todo_items.append(todo_item)
        else:
            raise Exception(
                f"ToDo item must be of datatype Todo_Item not {type(todo_item)}")

    def create_todo_item(self, task: str, priority: str = None, done: bool = False):
        item = Todo_Item(task, priority, done)
        self.todo_items.append(item)

    def search_todo_item(self, query):
        output = []

        for item in self.todo_items:
            if query.lower() in item.task.lower():
                output.append(item)

        return output

    def list_todo_items(self, priority: str = "All", done: bool = None, sort: bool = False):
        output1 = []
        
        for item in self.todo_items:
            if (done == True) and (item.done == True):
                output1.append(item)
            elif (done == False) and (item.done == False):
                output1.append(item)
            elif (done == None):
                output1.append(item)

        output2 = []

        if priority == "All":
            output2 = output1
        else:
            for item in output1:
                if priority == item.priority:
                    output2.append(item)

        
        if sort:
            priority_dict = {
                "High":[],
                "Medium":[],
                "Low":[],
                None:[],
                "Finished":[]
            }
            for item in output2:
                if item.done:
                    priority_dict["Finished"].append(item)
                else:
                    priority_dict[item.priority].append(item)
            
            output3 = priority_dict["High"] + priority_dict["Medium"] + priority_dict["Low"] + priority_dict[None] + priority_dict["Finished"]
        else:
            output3 = output2

        return output3

    # goes to the number and finishes that task
    def finish_todo_item(self, number):
        if number <= len(self.todo_items):
            for i in range(0, len(self.todo_items)):
                if i + 1 == number:
                    que = self.todo_items[i]
                    que.finish()
                    print(f"{que} task has been marked done")
                    break
        else:
            print(f"You have only {len(self.todo_items)} tasks")

    # deletes the number item
    def delete_todo_item(self, number):
        if number <= len(self.todo_items):
            for i in range(0, len(self.todo_items)):
                if i + 1 == number:
                    self.todo_items.pop(i)
                    break
        else:
            print(f"You have only {len(self.todo_items)} tasks")  