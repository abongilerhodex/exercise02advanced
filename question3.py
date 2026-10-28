# Question 3: Grading with Adjustments

user_score = int(input("Enter test score (0-100): "))
 

new_score = user_score + 5 - 10

final_score = max(0, min(100, new_score))
if user_score > 100:
 print(f"Invalid input! Enter valid score.")

elif final_score >= 90:
  print("Grade: A ")
elif final_score >= 80:
  print("Grade: B ")
elif final_score >= 70:
  print("Grade: C ")
elif final_score >= 80:
  print("Grade: B ")
else:
  print("Grade: F ")






