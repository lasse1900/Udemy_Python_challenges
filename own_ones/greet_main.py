def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # This code will only run if the script is executed directly, not when imported as a module
    user_name = input("Enter your name: ")
    greet(user_name)
