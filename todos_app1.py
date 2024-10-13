import json
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
    todo = input(f"Insert Task: ")
    while todo.lower() != "stop":
        task.append(todo)
        todo = input(f"Insert task: ")
        

def delete():
    task_delete = int(input("delete task number: ")) - 1
    task.pop(task_delete)
    return main()
    

def display():
        #print(f"Selamat Datang {fullname}, task Anda adalah:")
        num = 1
        print(f"There are your tasks:")
        for i in task:
            print(f"{num}.{i}")
            num += 1
        print(f"Hello {fullname}, you have: {len(task)} tasks\n")
        return main()

def _exit():    
    exit_ = input("Do you want to exit (y/n) : ")
    if exit_ == 'y':
        print("Thank you :)")
        d = {"Task": task}
        with open("todos.json", "w") as file:
            json.dump(d, file)
        exit()
    else:
        print("Please add your task: ")
        data()
        display()

     
def main():
    menu()
    try:
            user_input = int(input("Insert your choice : "))
            if user_input == 4:
             _exit()
            if user_input in [1,2,3]:
                if user_input == 1:
                    #print("1. Tambahkan task")
                    data()
                    main()
                elif user_input == 2:
                    display()
                    try:
                     if not task:
                        print("No tasks, please add your task\n")
                        return main()
                    except NameError:
                        print("No tasks, please add your task")          
                elif user_input == 3:
                    if not task:
                        print("No tasks, please add your task")
                        return main()
                    else:
                     delete()
    except ValueError:
        print("Input must be a number")


if __name__ == "__main__":
 user_input = int
 task = []
 main()