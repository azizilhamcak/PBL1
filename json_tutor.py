import json

with open('data.json', 'r') as file:
    data = json.load(file)
#print(data, type(data))
#print(data['members'])

data1 = {"todos": ["task1", "task2", "task3"]}
with open('data2.json', 'w') as file:
    json.dump(data1, file)
