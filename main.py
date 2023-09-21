# #######################################Dictionaries###############################
# # dictionary = a collection of {key:value} pairs with no duplicates
# # Dictionaries Practice #1
# # Create a dictionary called fruits with the following key-value pairs:
# # apple --> red
# # banana --> yellow
# # mango --> green
# # cherry --> red
# # watermelon --> green
# # # Display the dictionary on the screen.
# # capitals = {"USA": "Washington D.C",
# #             "India": "New Delhi",
# #            "China": "Beijing",
# #            "Russia": "Moscow"}
# # # print(dir(capitals))
# # # print(help(capitals))
# # print(capitals.get("USA"))
# # print(capitals.get("India"))
# # print(capitals.get("China"))
# # print(capitals.get("Russia"))

# # below is a nested list
# list1 = [[1,2,3],[4,5,6],[7,8,9]]

# print(list1[1][2]) # print 6
# print(list1[2][2]) # prints 9
# print(list1[0][2]) # prints 3

# car = {"color": "red",
#       "make": "ford",
#       "model": {"model1": "mustang",
#                "model2": "fusion",
#                "model3": "focus",
#                "model4": [1999,2000,2005]}}
# print(car["make"])
# print(car["color"])
# print(car["model"]["model4"][1])
# print(car["model"]["model3"])
# print(car.keys) # prints keys
# print(car.values) # prints values
# print(car.items) # prints both
# car["mileage"] = 120000
# print(car)
# car["serial number"] = 18921346782
# print(car)
# car["number of owners"] = 12
# print(car)

fruits = {"apple": "red",
         "banana": "yellow",
         "mango": "green",
         "cherry": "red",
         "watermelon": "green"}
print(fruits.get("apple"))
print(fruits.get("banana"))
print(fruits.get("mango"))
print(fruits.get("cherry"))
print(fruits.get("watermelon"))
fruits["banana"] = "green"
print(fruits.get("banana"))


# Dictionaries Practice #1
# Create a dictionary called my_dict that stores the following information about a person:
# name: Karen
# surname: Jurgens
# age: 35
# occupation: Journalist
# The names of the keys and values must be equal to the ones indicated above.
my_dict = {
    "name": "Karen",
    "surname":"Jurgens",
    "age":"35",
    "occupation":"Journalist",
  }

#   Dictionaries Practice #2
# Use print to returns the second item of the list called points2, inside the following dictionary.
# If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
my_dict1 = {"values_1":{"v1":3,"v2":6},
            "points":{"points1":9,"points2":[10,300,15]}}
print(my_dict1["points"]["points2"][1]) #Use dictionary indices to extract the second item of points2



# Dictionaries Practice #3
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:
# name: Karen
# surname: Jurgens
# age: 36
# occupation: Editor
# country: Colombia
# to do this, you should not change the line of code already written, but update the values using dictionary methods.
# my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict['country']= "Columbia"
my_dict["occupation"] = "Editor"
my_dict["age"] = "36"
print(my_dict)
