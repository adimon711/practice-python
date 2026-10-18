# Create an empty dictionary to start
grades = {}

# Phase 1: Gather the data
while True:
    name = input("Enter student name (or type 'stop'): ")
    
    if name == "stop":
        break  # This stops the while loop!
        
    try:
        score = int(input(f"Enter score for {name}: "))
    except ValueError:
        print('Error: you must enter values like actual digits eg:80,65...')
        continue  # This instantly skips the rest of the loop and asks for the next name!
    # If the try block succeeds, it ignores the except block and reaches here safely
    grades[name] = score

# Phase 2: Display the data
print("\n--- Final Class Grades ---")
for name, score in grades.items():
    print(f"{name} scored {score}")


#Making a calculator from this:
print("\n--- Overall Class Average ---")
total= sum(grades.values())
n= len(grades)
try:
    average= total/n
    print(f'Average of the class is: {average}')
except ZeroDivisionError:
    print('Error: Cannot divide by 0')
