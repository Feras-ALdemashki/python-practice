import json
json_file_name= "todo_list.json"

def add_task():
    try:
        with open(json_file_name,"r") as file:
            
            data= json.load(file)
            return data
    except:
        return {"tasks":[]}


def main():
   tasks= add_task()
   print(tasks)

main()