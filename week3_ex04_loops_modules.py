Fruits=("apple", "banana", "guava", "pear", "grape")

for fruit in Fruits:
  print(fruit)

#while loop for count down
i=5
while i>=1:
  print(i)
  i=i - 1
  #using for loop with range

  for i in range(11):
    print(i * i)
import random
colours=("blue", "red", "orange", "red", "pink", "black", "white")
print(random.sample(colours, 3))

#Create and use  a custom module
import math_operations
while True:
  choice = input("type 'calculator' to calculate or 'q' to quit:")
  if choice== 'q':
    break

  num1=float(input("Enter first number: "))
  num2=float(input("Enter second number: "))

  print("Addition:", math_operations.add(num1, num2))
  print("multiplication:", math_operations.multiply(num1, num2))