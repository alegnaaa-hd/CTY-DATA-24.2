list_of_objects = ["Pizza","Ice Cream", "Chips"]

food_name = input("Enter your food choice? :")

found = False
for food in list_of_objects:
    if food_name == food:
        found = True 
        break
if found: # if found == True:
    print("We found your choice", food_name)
else:
    print("Sorry!")