Q = 1 Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal

sugar = int(input("Enter the fastest suger level"))
sugar = float(sugar)
if sugar < 80:
    print("Your sugar is low")
elif sugar > 100:
    print("Your sugar is high")
else:
    print("Your sugar is normal ")
    
Q = 2 A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A

grade = int(input("Enter the marks:\n"))
grade = float(grade)

if grade <= 25:
    print("your grade is F")
elif grade >= 25 and grade <= 45:
    print("Your grade is E")
elif grade >= 45 and grade <= 50:
    print("Your grade is D")
elif grade >= 50 and grade <= 60:
    print("Your grade is C")
elif grade >= 60 and grade <= 80:
    print("Your grade is B")
else:
    print("Your grade is A")
    
    
Q = 4 11.A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.

Ans   nch = float(input("Number of classes held:\n"))
      nca = float(input("Number of classes attended"))
      percentage = (nca/nch)*100
      print(percentage)

if percentage <= 75:
    print("You are not sit in exam")
else:
    print("You are sit in exam")
    
Q = 5 

    
    
