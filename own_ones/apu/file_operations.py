# file_operations.py
# 
# The if __name__ == "__main__": construct is commonly used in Python to create reusable modules and scripts. It allows you to write code that can be both imported as a module into other scripts and executed as a standalone script. Here's a real-world usage example:
# Suppose you're developing a utility module for working with files and directories, and you want to include functions for common file operations. You want the module to be importable into other Python scripts, but you also want to provide a way to use it as a standalone tool for specific tasks. Let's create a simple example for this scenario:
# Usage e.g. give input: [C:\Users\lauri\eclipse-workspace]    

import os

def list_files_in_directory(path):
    files = os.listdir(path)
    for file in files:
        print(file)

def create_directory(directory_name):
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created.")

if __name__ == "__main__":
    # Code that only runs when the script is executed directly
    action = input("Choose an action (list/create): ")

    if action == "list":
        directory_path = input("Enter the directory path: ")
        list_files_in_directory(directory_path)
    elif action == "create":
        directory_name = input("Enter the directory name to create: ")
        create_directory(directory_name)
    else:
        print("Invalid action. Choose 'list' or 'create'.")
