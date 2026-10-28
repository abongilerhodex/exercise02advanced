# Question 1
import math

#variables
a = 5
b = 10
c = 7

a += 3
b *= 2
c %= 4 

squareroot_sum = math.sqrt(a ** 2 + b ** 2 + c ** 2)

round_result = round(squareroot_sum, 2)

print("Final result: " + str(round_result))