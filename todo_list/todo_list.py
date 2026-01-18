import json
json_file_name= "todo_list/todo_list.json"

def load_task():
   
        with open(json_file_name,"r") as file:
            
            data= json.load(file)
            return data
   
def view_tasks(tasks):
   for i, task in enumerate(tasks["tasks"], start=1):
    status = "complete" if task["complete"] else "not complete"
    print(f"{i}. {task['description']} — {status}")

def add_task(tasks):
    task = input("please enter the task: ").strip()
    if task:
       tasks["tasks"].append({"description":task,"complete":False})
    else:
       print("please enter a task")
    with open(json_file_name,"w") as file:
            json.dump(tasks,file)
def delete_task(tasks):
    try:
        task_index = int(input("please select task number: ").strip())
    except ValueError:
        print("please enter a valid number")
        return

    task_number = task_index - 1
    task_list = tasks.get("tasks", [])

    if task_number < 0 or task_number >= len(task_list):
        print("no task with this number")
        return

    removed = task_list.pop(task_number)

    with open(json_file_name, "w") as file:
        json.dump(tasks, file, indent=2)

    print(f"deleted: {removed['description']}")
def mark_task_complete(tasks):
    try:
        task_index = int(input("please select task number to mark complete: ").strip())
    except ValueError:
        print("please enter a valid number")
        return

    task_number = task_index - 1
    task_list = tasks.get("tasks", [])

    if task_number < 0 or task_number >= len(task_list):
        print("no task with this number")
        return

    task_list[task_number]["complete"] = True

    with open(json_file_name, "w") as file:
        json.dump(tasks, file, indent=2)

    print(f"marked complete: {task_list[task_number]['description']}")

def main():
   tasks= load_task()
   while True:
    print("type 1 to view tasks\ntype 2 to add a task\ntype 3 to delete a task\ntype 4 to mark task as completed\ntype 5 to exit")
    user_choice=input("Please enter your choice: ").strip()
    if user_choice == "1":
     view_tasks(tasks)
    elif user_choice == "2":
      add_task(tasks)
    elif user_choice =="3":
      delete_task(tasks)
    elif user_choice == "4":
      mark_task_complete(tasks)
    elif user_choice == "5":
      print("Goodbye")
      break
    else:
       print("please choose a number between 1 and 5")



main()