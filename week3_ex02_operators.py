#Arimethic and Assignment Operators

x=8
y=9
x+=3
y/=2
result=x/y
print(result)

#comparison and logical operators

a=10
b=6
c=12
if a>b:
  print("correct")
else:
  print("Incorrect")
if b % 2 == 0:
  print("b is even")
else:
    print("b is odd")
if c<=a:
  print("correct")
else:
  print("incorrect")
Final_condition=(c<=a) or ((b%2==0) and (a>b))
print(Final_condition)

#conditional statements

score=84
if score>=90:
  print("Grade: A")
elif score>=80:
  print("Grade: B")
elif score>=70:
  print("Grade: C")
elif score>=60:
  print("Grade: D")
else:
  print("F")

#Combining operators and Conditionals
num1=22
num2=15
operation="*"
if num1 * num2>=300:
  print("The result is 300 or more")
else:
  print("The result is less than 300")
