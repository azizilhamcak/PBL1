import json
import pandas as pd

def name():
    print("-------------------")
    print("TO-DO LIST APP")
    print("-------------------\n")
    name1 = input("First Name : ")
    name11 = input("Last Name : ")
    return f"{name1} {name11}"

def displayname(fullname):
    print(f"\n Welcome {fullname} \n") 

fullname = name()
displayname(fullname)
   
def menu():
    print("1. Add Task")
    print("2. Show Task")
    print("3. Delete Task")
    print("4. Exit")

def data():
    while True:
        n = int(input("Enter number of tasks: "))
        for _ in range(n):
            todo = input(f"Insert Task: ")
            description = input(f"Description your task: ")
            isImportant = input(f"Is your task {todo} important 1 or 0: ")
            if isImportant == "1":
                isImportant = True
            elif isImportant == "0":
                isImportant = False
            notes = input(f"Notes your task: ")
            todos.append({"task": todo, "description": description, "isImportant": isImportant, "notes": notes})
        return menu()

def delete():
    task_delete = int(input("delete task number: ")) - 1
    todos.pop(task_delete)
    return main()
    

def display():
    #print(f"Selamat Datang {fullname}, task Anda adalah:")
    print(f"Hello {fullname}, you have: {len(todos)} tasks\n")
    df = pd.DataFrame(todos)
    df.index += 1
    print(df)
    print("\n")
    return main()

def save_data():
    d = {"Task": todos}
    with open("todos.json", "r") as file:
        ex_data = json.load(file)
        ex_data["Task"].extend(d["Task"])
    with open("todos.json", "w") as file:
        json.dump(ex_data, file, indent=4)
                           
def _exit():    
    exit_ = input("Do you want to exit (y/n) : ")
    if exit_ == 'y':
        save_data()
        exit()
    else:
        print("Please add your task: ")
        data()
        display()

     
def main():
    menu()
    while True:
        try:
                user_input = int(input("Insert your choice : "))
                if user_input == 4:
                    _exit()
                    break
                if user_input in [1,2,3]:
                    if user_input == 1:
                        #print("1. Tambahkan task")
                        data()
                    elif user_input == 2:
                        display()
                        try:
                            if not todos:
                                print("No tasks, please add your task\n")
                                #return main()
                        except NameError:
                                print("No tasks, please add your task")          
                    elif user_input == 3:
                        if not todos:
                            print("No tasks, please add your task")
                            #return main()
                        else:
                            delete()
        except ValueError:
            print("Input must be a number")
            continue

if __name__ == "__main__":
 user_input = int
 todos = []
 main()
 