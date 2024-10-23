# Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
# If there are multiple elements with the same value, remove the one with the lowest index. 
# If you get an empty array/list, return an empty array/list.
# Don't change the order of the elements that are left.

# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]

def remove_smallest(numbers):
    if not numbers:
        return []
    lowest_num = min(numbers)
    lowest_num_index = numbers.index(lowest_num)
    new_list = numbers[:lowest_num_index] + numbers[lowest_num_index + 1:]
    
    # numbers.remove(lowest_num)
    return new_list
    

print(remove_smallest([5,3,2,1,4,1]))