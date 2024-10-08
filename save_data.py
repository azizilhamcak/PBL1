task = ['a', 'b', 'c']
with open("data.txt", "w") as file:
    file.writelines(task)

with open('output.txt', 'w') as file:
    for t in task:
        file.write(t + '\n')

with open('data.txt', 'r') as file:
    out = file.read()

print(out)