# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
# You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    bin_num = bin(n)[2:]
    count = bin_num.count('1')
    return count

    

print(count_bits(1234))