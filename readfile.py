with open('todolist.txt', 'r') as file:
    lines =file.readlines()
    print("My Todo list:")
    for task in lines:
        print(f" - {task.strip()}")


