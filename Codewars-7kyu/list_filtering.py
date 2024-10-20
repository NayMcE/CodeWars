# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
    return [i for i in l if isinstance(i, int)]
        

print(filter_list([1, 2,'a','b']))


def is_valid_walk(walk):
    dict = {}
    for item in walk:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    # add the values in the list to the dictionary 
    # new_dict = {key: value for key, value in dict.items() if value > 1}
    # check if the values are the same
    result = True
    test_val = list(dict.values())[0]
    for ele in dict:
        if dict[ele] != test_val:
            result = False
            break
    return result
    
print(is_valid_walk(['n','n','n','s','s','s']))