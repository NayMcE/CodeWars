# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

def digital_root(n):
    # split the integars in n to add together
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


print(digital_root(132189))