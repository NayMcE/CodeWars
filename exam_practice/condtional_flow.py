# TASK 1 (Conditional flow)

# Question 1
# Create a program that tells you whether or not you need sunglasses when you leave
# the house.
# The program should:
# 1. Ask you if it is sunny using input()
# 2. If the input is 'y', it should output 'Take your sunglasses’
# 3. If the input is 'n', it should output 'You don't need sunglasses’

# def sunglasses():
#     sunny = input('Is it sunny today? Type y for yes, and n for no ').lower()
#     if sunny == 'y':
#         print('Take your sunglasses')
#     elif sunny == 'n':
#         print('You dont need sunglasses')

# (sunglasses())

# def hire_affordability():
#     my_money = input('How much money do you have? ') 
#     my_money_int = int(my_money)
#     hour = 3
#     venue_cost = (200 * hour) + 1.1

#     if my_money_int < venue_cost:
#         print('You can afford the venue')
#     else:
#         print('You cannot afford the venue')

# hire_affordability()

# best practice is to put the code into a function to avoid all code being on the global scope. 
# the venue cost variable had a space and needed an underscore to allow python to read the variable.
# the if statement would not run as it was comparing a str input with an integar so added an additional variable to convert the input into a integar.

# You work as a primary school teacher and are teaching numbers by showing how
# they are composed of units of ten and one. Write a program for students to play with
# to understand this concept. You will be asking for them to enter numbers between 1
# and 25 (they haven’t gone higher than that!), so you do not need to consider bigger
# numbers. The function needs to print to the screen and the message must be
# grammatically correct and in the format shown below.

# def tens_and_ones(int):
#     tens = int // 10 % 10
#     ones = int % 10    
#     return f'This number has {tens} tens and {ones} ones'

# print(tens_and_ones(8))

students = ['Chloe', 'Anna', 'Lauren', 'Shreya', 'Siobhan']
print(sorted(students)[1])

# Create a ‘shop’ dictionary with at least 4 items and respective prices. ●
# Write some code that will take in the name of an item and output the price

def bootsale(items):
    items = {'picture':10.00, 'rocking_horse':5.00, 'weights': 15.00, 'tv':30.00}
    return items.fromkeys()

print(bootsale('picture'))