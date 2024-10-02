# def feast(beast, dish):
#     beast_first_char = beast[0], beast[-1]
#     dish_first_char = dish[0], dish[-1]
#     acceptable_offering = beast_first_char == dish_first_char
#     if acceptable_offering == True:
#         print('You may bring this dish')
#     else:
#         print('This doesnt match, you cant bring this dish')
#     return acceptable_offering

# print(feast('snake','soup'))

#faster way of doing it 
def feast(beast, dish):
    return beast[0]==dish[0] and dish[-1]==beast[-1]