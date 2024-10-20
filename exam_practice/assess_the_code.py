# Description:
# Your goal in this is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]

# def array_diff(a, b):  
#     my_list = []
#     for y in a:
#         if y not in b:
#             new_list.insert(y)
#     print(new_list)

# print(array_diff([1,2,3],[1,2]))

# returning unique numbers from two lists.
# the variable name is incorrect when trying to insert into the list. the variable at the top is called my_list but then later it is called new_list. new_list needs to be changed
# to my_list to call it.same then in the print we need to change this to be my_list.
# instead of using insert we need to use the append method which will add the number to my_list. With the insert you would need to specify where we want the number to go in the list
# which in this case we are not doing. 
# need to use a return statement rather than print as we always need to return something in python or we will get a None in the console after the function has run.

def array_diff(a, b):  
    my_list = []
    for y in a:
        if y not in b:
            my_list.append(y)
    return my_list

print(array_diff([1,2,6,4,5],[1,2]))