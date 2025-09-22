'''# Missing colon in if statement
x = 10
if x >5
    print("x is greater than 5")

x = 10
if x > 5:   # added colon
    print("x is greater than 5")'''


'''try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
    
    Enter numerator: 10
Enter denominator: 0
Error: Division by zero is not allowed!''' 


'''try:
    age = int(input("Enter your age: "))
    print("You are", age, "years old.")
except ValueError:
    print("Error: Please enter a valid number for age.")

Enter your age: 25
You are 25 years old.

Enter your age: twenty
Error: Please enter a valid number for age.'''


'''try:
    num = 10
    text = "5"
    result = num + text   # this will raise TypeError
    print("Result:", result)

except TypeError:
    print("Error: You cannot add an integer and a string directly.")

Error: You cannot add an integer and a string directly.

num = 10
text = "5"
result = num + int(text)
print("Fixed Result:", result)'''


'''try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Error: That’s not a valid integer.")

finally:
    print("Program Completed")

Enter an integer: 42
You entered: 42
Program Completed

Enter an integer: hello
Error: That’s not a valid integer.
Program Completed'''



'''try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")

Enter numerator: 10
Enter denominator: 2
Result: 5.0

Enter numerator: 10
Enter denominator: 0
Error: Division by zero is not allowed.

Enter numerator: ten
Enter denominator: 2
Error: Please enter valid numbers.'''

'''try:
    with open("student_data.txt", "r") as file:
        data = file.read()
        print("File contents:\n", data)

except FileNotFoundError:
    print("Error: The file 'student_data.txt' was not found.")

Error: The file 'student_data.txt' was not found.

File contents:
John, 21
Emma, 22
Liam, 20'''


'''try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)

except Exception as e:   # catch any unexpected error
    print("An error occurred:", e)

Enter a number: 6
Square: 36

Enter a number: hello
An error occurred: invalid literal for int() with base 10: 'hello'''

'''try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")  # custom error
    print("Your age is:", age)

except ValueError as ve:
    print("Error:", ve)

Enter your age: 25
Your age is: 25

Enter your age: -5
Error: Age cannot be negative!'''



def safe_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Choose operation: +, -, *, /")
        op = input("Enter operation: ")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        else:
            print("Error: Invalid operation!")
            return

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Run the calculator
safe_calculator()

Enter the first number: 10
Enter the second number: 5
Choose operation: +, -, *, /
Enter operation: *
Result: 50.0
division by zero:
Enter the first number: 10
Enter the second number: 0
Choose operation: +, -, *, /
Enter operation: /
Error: Division by zero is not allowed.

invalid number input:
Enter the first number: ten
Enter the second number: 5
Choose operation: +, -, *, /
Enter operation: +
Error: Please enter valid numbers.






