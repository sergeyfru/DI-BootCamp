
# Exercise 1 
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_numbers = {3,15,8,40}
# my_fav_numbers.add(817)
# my_fav_numbers.add(430)
# my_fav_numbers.remove(817)
# print(my_fav_numbers)
# friend_fav_numbers = {10,18,32,40}
# our_fav_numbers = my_fav_numbers | friend_fav_numbers
# print(our_fav_numbers)

#  Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

            # NO
            
#  Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove('Banana')
# basket.remove("Blueberries")
# basket.append('Kiwi')
# basket.insert(0,'Apples')
# print(basket)
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# counter = 0
# for fruit in basket:
#     if fruit == "Apples":
#         counter +=1
# print(counter)

# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

# numb_list = [1.5,2,2.5,3,3.5,4,4.5,5]
# print(numb_list)

# numb_list2 = []
# num = 1.0
# while num <= 5:
#     numb_list2.append(num)
#     num += 0.5
# print(f'List2 {numb_list2}')

# Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# for x in range(1,21):
#     print(x)

# index_num = 0
# for x in range(1, 21):
#     if index_num % 2 == 0:
#         print(x)
#     index_num +=1

# Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# while True:
#     user_name = input('Guess my name! ').capitalize()
#     if user_name == 'Sergey':
#         print('Congratulations!!!')
#         break
#     else:
#         print('Try one more time.')

# Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# user_input = input('What is your favorif fruite?(if you have several fruits, please separate the fruits with a single space): ')
# list_of_fruits = user_input.split()
# user_input2 = input('Chose any fruit. ')
# if user_input2 in list_of_fruits:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#     print('You chose a new fruit. I hope you enjoy')
    
    
#     Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

# pizza = []
# price = 10
# while True:
#     user_input = input('What you want to add in pizza? ')
#     if user_input == 'quit':
#         pizza_toppings = ", ".join(pizza)
#         print(f'You ordered pizza, toppings will be: {pizza_toppings}.\nThe price is {price}')
#         print('Thank you for order')
#         break
#     else:
#         pizza.append(user_input)
#         price += 2.5
        
# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

user_input_age = input('What is the age of persons: ')