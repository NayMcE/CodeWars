# def high_and_low(numbers):
#     data = [int(number) for number in numbers.split(' ')]
#     return '%i %i' % (max(data), min(data))

# print(high_and_low('1 2 3 4 5'))



def high_and_low(numbers):
    numbers = [int(num) for num in numbers.split(' ')]
    return f"{max(numbers)} {min(numbers)}"

print(high_and_low('1 2 3 4 5'))

