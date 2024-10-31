import json
import pandas as pd
def name():
    print("-------------------")
    print("myERP mini apps")
    print("-------------------\n")
    name1 = input("First Name : ")
    name11 = input("Last Name : ")
    return f"{name1} {name11}"

def displayname(fullname):
    print(f"\n Welcome {fullname} \n") 

fullname = name()
displayname(fullname)
   
def menu():
    print("1. Add Item")
    print("2. Show Item")
    print("3. Delete Item")
    print("4. Exit")

def data():
       n = int(input("Enter number of pairs: "))
       for _ in range(n):
              item_ = input("Enter item_: ")
              price = int(input("Enter price: "))
              stock = input("Enter stock: ")
              key_value_list.append({"item_": item_, "price": price, "stock": stock})

def delete():
    key_value_list_delete = int(input("Delete item number: ")) - 1
    key_value_list.pop(key_value_list_delete)
    return main()
    

def display():
        #print(f"Selamat Datang {fullname}, task Anda adalah:")
        num = 1
        print(f"There are your items:")
        for i in key_value_list:
            print(f"{num}.{i}")
            num += 1
        print(f"Hello {fullname}, you have: {len(key_value_list)} items\n")
        df = pd.DataFrame(key_value_list)
        df.index += 1
        print(df)
        return main()

def _exit():    
    exit_ = input("Do you want to exit (y/n) : ")
    if exit_ == 'y':
        print("Thank you :)")
        d = {"Items": key_value_list}
        with open("todos.json", "w") as file:
            json.dump(d, file)
        exit()
    else:
        print("Please add your items: ")
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
                     if not key_value_list:
                        print("No tasks, please add your task\n")
                        return main()
                    except NameError:
                        print("No tasks, please add your task")          
                elif user_input == 3:
                    if not key_value_list:
                        print("No tasks, please add your task")
                        return main()
                    else:
                     delete()
    except ValueError:
        print("Input must be a number")


if __name__ == "__main__":
 user_input = int
 key_value_list = []
 main()
