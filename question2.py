# Question 2: Complex Conditional Evaluation

x = float(input("Enter value for x: "))
y = float(input("Enter value for y: "))
z = float(input("Enter value for z: "))

# condtions
is_even = (x % 2 == 0)
is_positive = ( y>0 )
is_in_range = ( 10 <= z <=50 )


final_condition = is_even and is_positive and is_in_range
print(final_condition)
