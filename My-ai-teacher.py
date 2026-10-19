print("Welcome to My AI Learning Assistant!")

name = input("What is your name? ")

print(f"Hello {name}! Welcome to your AI learning journey.")

print("\nWhat would you like to learn today?")
print("1. Artificial Intelligence")
print("2. Python Coding")
print("3. Automation")
print("4. Sales and Communication")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Start by learning what AI is and how it works.")
elif choice == "2":
    print("Start with Python variables, inputs, and outputs.")
elif choice == "3":
    print("Start by learning how to automate repetitive tasks.")
elif choice == "4":
    print("Start by practising communication and sales conversations.")
else:
    print("Please choose a number between 1 and 4.")
