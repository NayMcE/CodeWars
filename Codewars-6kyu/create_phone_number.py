# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    # use index to position the numbers in a new string.
    return f'({n[0:3]})' + ' ' + f'{n[3:6]}' + '-' + f'{n[6:]}'
    

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))