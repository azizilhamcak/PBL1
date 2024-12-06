import json

def save_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
    

def login(db):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in db and db[username]['password'] == password:
        print("Login Successful")
        return db[username]
    else:
        print("Login Failed")

if __name__ == "__main__":
    db = save_data('data.json')
    login(db)
    