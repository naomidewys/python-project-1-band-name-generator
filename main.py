import art

#Add header / greeting
print(art.logo)
print("Welcome to the Band Name Generator.")
print("Create a band name by answering the following questions.")

#Create answers from these questions
city_name = input("What city did you grow up in?\n")
pet_name = input("What is the name of your first pet?\n")

#Generate band name
print("Your band name is " + city_name + " " + pet_name + "!")
