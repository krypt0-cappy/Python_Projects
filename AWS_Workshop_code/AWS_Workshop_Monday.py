# AWS Workshop: Monday
# Data Types

# STRINGS
first_name = "Todd"
last_name = "Caputo"

print(first_name + " " + last_name)

# Using Variables in strings

print("My first name is {}. My last name is {}.".format(first_name, last_name))


# f strings
print(f"My first name is {first_name}. My last name is {last_name}.")


# NUMBERS
my_age = 41
how_old = "My age is: "
print(how_old + str(my_age))


# DICTIONARIES
user = {"first_name":"Todd", "last_name":"Caputo", "age":"41"}
print(user)

# Modify a dictionary value
user["middle_name"] = "Keith"
print(user)

# Remove a dictionary value
del user["age"]


# LISTS

# Create a list
fruit = ["apples", "bananas", "cherries", "oranges", "kiwis"]
print(fruit)
print(fruit[3])

# Create a list a different way
fav_foods = []
fav_movies = list()

# Find the length of a list
list_length = len(fruit)
print(list_length)

# Update a list
fav_foods.append("Pizza")
fav_foods.append("Burgers")

fav_movies.append("Iron Man")
fav_movies.append("Thor")

fav_foods.insert(2, "Tacos")
fav_movies.insert(0, "Captain America")

print(fav_foods)
print(fav_movies)

# Organizing a list
print(fav_foods)
print(sorted(fav_foods))
print(fav_movies)
print(sorted(fav_movies))

#Permanent Sort a List
fav_foods.sort()
fav_movies.sort()
print(fav_foods)
print(fav_movies)


#Reverse the order of a list
fav_foods.reverse()
fav_movies.reverse()
print(fav_foods)
print(fav_movies)

#Delete an item from a list
del fav_foods[2]
del fav_movies[0]
print(fav_foods)
print(fav_movies)


