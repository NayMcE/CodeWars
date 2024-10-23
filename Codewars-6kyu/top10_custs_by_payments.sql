def remove_smallest(numbers):
    if not numbers:
        return []
    lowest_num = min(numbers)
    lowest_num_index = numbers.index(lowest_num)
    new_list = numbers[:lowest_num_index] + numbers[lowest_num_index + 1:]
    
    # numbers.remove(lowest_num)
    return new_list