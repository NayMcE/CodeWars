def string_to_array(s):
    split_string = s.split()
    # return the split string into an array
    if s == '':
        return ['']
    return split_string

print(string_to_array('sally'))
