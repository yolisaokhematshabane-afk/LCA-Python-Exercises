# creating and modifying lists

Fruits=["banana", "orange", "apple", "grape", "peach", "tomato", "pear"]
Fruits.append("mango")
Fruits.insert(0, "pineple")
Fruits.remove("tomato")
print("Modified Fruit list:", Fruits)

#List operat1ions

numbers=[1, 2, 3, 4, 5]
squared_numbers=[num ** 2 for num in numbers]
total_sum= sum(numbers)
average=total_sum
print(average)

#creating and modifiying dictionarie
capitals={"South Africa":  "johhanersburg", 
          "Egypt":  "Cairo",
          "Emirate of Dubai":  "Dubai",
          "China":  "Beijig"}
capitals["Canada"]= "Ottawa"
capitals["Egypt"]= "Alexandra"
del capitals["Canada"]
print("Modified dictionary", capitals)

#Dictionary operations
fruit_colours={"apple":  "red", 
               "orange": "orange",
               "banana":  "yellow",
               "pear": "green"}
print("fruits:", list(fruit_colours.keys()))
print("fruits:", list(fruit_colours.values()))
print("\n--- Fruit Colors List ---")
for fruit, color in fruit_colours.items():
  print(f"The {fruit} is {color}.")

#search and print the color

search_fruit="banana"
print("\n--- Checking for a fruit---")
if search_fruit in fruit_colours:
  print(f"Yes! {search_fruit} is in the dictionary, and its color is {fruit_colours[search_fruit]}.")
else:
  print(f"Sorry, {search_fruit} is not found.")