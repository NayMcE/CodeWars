def add_binary(a,b):
    number_result = a + b
    binary_result = bin(number_result)
    binary_stripped = binary_result.lstrip('-0b')
    return binary_stripped

print(add_binary(1, 1))