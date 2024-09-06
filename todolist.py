
tasks= []

while True:
    print("\n--------TO DO LIST----------")
    print("1.ADD TASK")
    print("2.SHOW TASK")
    print("3.MARK TASK AS DONE")
    print("4.EXIT")
    
    choice=input("Enter your choice: ")
    if choice=='1':
                print()
                n_tasks=int(input("Enter the no. of tasks you want to add: "))
                for i in range(n_tasks):
                       task=input("Enter the task: ")
                       tasks.append({"task":task, "done":False})
                       print("Task Added")
    elif choice=='2':
                print("\nTASKS")
                for index,task in enumerate(tasks):
                        status="Done" if task["done"] else "Not Done"
                        print(f"{index+1}. {task['task']}-{status}")
    elif choice=='3':
                task_index=int(input("enter the task no. you want to mark as done"))-1
                if 0<=task_index<len(tasks):
                    tasks[task_index]["done"]=True
                    print("Marked as done")
                else:
                    print("Invalid task no.")
    elif choice=='4':
                print("Exit")
                break
    else:
            print("Invalid choice.Please try again!")

    

            
            