# This is the start of my Week 12 Project
# Creating an empty list to fill
my_aws_list = []

# Let's take our text string and make a variable to use later
List_Text = "This is a list of my favorite AWS Services so far: "
print(List_Text)

# Let's take our item count string and make a variable to use later
Item_Count_Text = "My list contains the following number of items: "
print(Item_Count_Text, len(my_aws_list), "\n")

# Using the append element to add a few items to our list
my_aws_list.append("S3")
my_aws_list.append("Cloud Formation")
my_aws_list.append("VPC")
my_aws_list.append("CodePipeline")
print(List_Text, my_aws_list)

# Print the lenth of the current list using the len parameter
print(Item_Count_Text, len(my_aws_list), "\n")

# Using the insert element to add a few items to our list in a specific order
my_aws_list.insert(3, "EC2")
my_aws_list.insert(4, "Cloud9")
my_aws_list.insert(5, "CodeBuild")
my_aws_list.insert(6, "RDS")
print(List_Text, my_aws_list)
print(Item_Count_Text, len(my_aws_list), "\n")

# Removing an item from the list using the remove parameter
my_aws_list.remove("S3")
print(List_Text, my_aws_list)
print(Item_Count_Text, len(my_aws_list), "\n")

# Removing an item from the list using the del parameter
del my_aws_list[3]

# Print the final list and current list count
print(List_Text, my_aws_list)
print(Item_Count_Text, len(my_aws_list), "\n")

print("Welcome to the end of our Week 12 Python Project!")

