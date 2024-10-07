# def abbrev_name(name):
#     split_name = name.split(' ')
#     first_name = split_name[0]
#     first_name_initials = first_name[0]
#     last_name = split_name[1]
#     last_name_intials = last_name[0]
#     initials = first_name_initials + '.' + last_name_intials
#     return initials.upper()



def abbrev_name(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

print(abbrev_name('paul falks'))