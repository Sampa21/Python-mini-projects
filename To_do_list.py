# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:56:40 2024

@author: Samruddhi
"""

tasks=[]
 
def add_task(task):
        tasks.append(task)
        print("Task added:", task)
        
def delete_task(task):
        if task in tasks:
            tasks.remove(task)
            print("Task deleted:" ,task)
        else:
            print("Task not found")
             
def view_task():
    if not tasks:
        print("No task in the list")
    else:
        print("Tasks:")
        #iterate over each task in the list and print its index and content
        for index, task in enumerate (tasks, start=1):
            print(f"{index}.{task}")

while True:
    print("options:")
    print("Enter 'add' to add task in the list")
    print("Enter 'delete' to delete task from the list")
    print("Enter 'View' to view task in the list")
    print("Enter 'exit' to exit to end the program")

    user_input= input(": ")
    
    if user_input == "exit":
        break
    elif user_input == "add":
        task = input("Enter a task:")
        add_task(task)
    elif user_input == "delete":
        task = input("Enter task to delete:")
        delete_task(task)
    elif user_input == "View":
            view_task()
    else:
         print("Invalid input")
    
        
            