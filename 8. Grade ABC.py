grade = input("Enter your grade (A, B, C, D, F): ")

if grade == 'A':
  print("Excellent job!")
elif grade == 'B':
  print("Good job!")
elif grade == 'C':
  print("You can do better.")
elif grade == 'D' or grade == 'F':
  print("You need to study more.")
else:
  print("Invalid grade.")