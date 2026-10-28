# Question 4: Advanced Calculator

num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))

operation = input("Enter operation (+, -, *, /, %, **): ")

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
   division = num1/num2
   print(division)
  except ValueError:
   print("Invalid input")
  except ZeroDivisionError:
   print("Cannot divide by zero!")


