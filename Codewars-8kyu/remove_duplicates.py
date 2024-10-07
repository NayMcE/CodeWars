# def distinct(seq):
#     my_list = list(dict.fromkeys(seq))
#     return my_list

# print(distinct([1, 1, 2]))

def distinct(seq):
    return list(set(seq))

print(distinct([1, 1, 2]))