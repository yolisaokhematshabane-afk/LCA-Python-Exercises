def greet():
  print("Hello World")
greet()

#function with parameters
def greeting(name):
  print("This is a personalized greeting, good day " + name)
greeting("Yolisa")

#function with return value
def square(number):
  return(number * number)
print(square(5))

#function with multiple parameters
def Rectangle_Area(Length, width):
 return(Length * width)
Length=4
width=5
print(Rectangle_Area(Length, width))

#function as argument
def apply_operation(function, number):
  return function(number)

def double(number):
  return number * 2 
print(apply_operation(double, 7))
print(apply_operation(square, 3))