# def vaporcode(s):
#     s_upper = s.upper()
#     split_string = list(s_upper.replace(' ',''))
#     delimiter = '  '
#     string_from_list = delimiter.join(split_string)
#     return string_from_list



# def vaporcode(s):
# #     first remove all spaces, to later add spaces equally
#     no_spaces = s.replace(" ", "")
# #     use .join to pass the criteria "  " double space
#     new_word = "  ".join(no_spaces).upper()
#     return new_word

def vaporcode(s):
    return '  '.join(c for c in s.upper() if c != ' ')

print(vaporcode('Hello Im naomi'))