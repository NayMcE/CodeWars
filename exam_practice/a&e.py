def waiting_time(amounts):
#     # first index will always be 0, then iterte through the integers in the list to add them together to get the total
    sorted_list = sorted(amounts)
    print(sorted_list)
    total = 0
    for num in sorted_list[1:]:
        total += num
    return total


print(waiting_time([3,2,1,2,6]))


