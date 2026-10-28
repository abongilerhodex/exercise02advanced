# Question 4: Advanced Calculator

num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))

# TODO: Input operation
operation = input("Enter operation (+, -, *, /, %, **): ")
# TODO: Match operation using if-elif
if operation == "+":
  print(num1 + num2)
elif operation == "-":
   print(num1 - num2)
elif operation == "*":
  print(num1 * num2)
elif operation == "%":
  try:
   modulus = num1%num2
   print(modulus)
  except ZeroDivisionError:
    print("Invalid entry. Try inputting value greater than zero")

elif operation == "/":
  try:
   result = num1/num2
   print(result)
  except ValueError:
   print("Invalid input")
  except ZeroDivisionError:
   print("Cannot divide by zero!")


