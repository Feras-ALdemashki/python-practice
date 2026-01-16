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
def delete_task():
   return 
    
def mark_task_complete():
   return

def main():
   tasks= load_task()
   print(tasks)
   while True:
    print("type 1 to view tasks\ntype 2 to add a task\ntype 3 to delete a task\ntype 4 to mark task as completed\ntype 5 to exit")
    user_choice=input("Please enter your choice: ").strip()
    if user_choice == "1":
     view_tasks(tasks)
    elif user_choice == "2":
      add_task(tasks)
    elif user_choice =="3":
      delete_task()
    elif user_choice == "4":
      mark_task_complete()
    elif user_choice == "5":
      print("Goodbye")
      break
    else:
       print("please choose a number between 1 and 5")



main()