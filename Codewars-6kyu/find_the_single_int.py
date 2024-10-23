# You are given an array (which will have a length of at least 3, but could be very large) 
# containing integers. The array is either entirely comprised of odd integers or entirely comprised 
# of even integers except for a single integer N. Write a method that takes the array as an argument 
# and returns this "outlier" N.

# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

def find_outlier(integers):
    even_ints = [num for num in integers if num % 2 == 0]
    odd_ints = [num for num in integers if num % 2 != 0]
    if len(even_ints) == 1:
        return even_ints[0]
    else:
        return odd_ints[0]
    
    # if len(even_ints) == 1:
    #     return even_ints
    # else:
    #     return odd_ints
    
print(find_outlier([2,6,8,200,700,1,84,10,4]))