
import emoji

todo_list = []

def display_todo_list():
    print("Todo List: ")
    for i, task in enumerate(todo_list):
        print(f"{i+1},{task}")

def add_task(task):
    todo_list.append(task)
    print(f"Task Added:{task}")

def remove_task(index):
    task = todo_list.pop(index-1)
    print(f"Task Removed:{task}")

while True:
    display_todo_list()
    print("OPTIONS : ")
    print("1 - ADD TASK")
    print("2 - REMOVE TASK")
    print("3 - QUIT")
    choice = int(input("ENTER YOUR CHOICE : "))

    if choice == 1:
        task = input("ENTER THE TASK : ")
        add_task(task)
    elif choice == 2:
        index =  int(input("ENTER THE TASK INDEX : "))
        remove_task(index)
    elif choice == 3:
        break
    else:
        print("INVALID CHOICE")


print("BYE!HAVE A NICE DAY")
print(emoji.demojize(':smiling_face:'))