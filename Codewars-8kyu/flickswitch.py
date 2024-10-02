def flick_switch(lst):
    flick = True
    returnarray = []
    for element in lst:
        if element == 'flick': flick = not flick
        returnarray.append(flick)
    return returnarray

print(flick_switch(['hello', 'world', 'flick', 'beam']))

