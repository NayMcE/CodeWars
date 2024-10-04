def count_sheeps(sheep):
    return sum([1 for s in sheep if s])

print(count_sheeps([True, True, False, True]))


