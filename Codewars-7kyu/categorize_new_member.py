def open_or_senior(data):
    categorization = []
    for new_member in data:
        if new_member[0] >= 55 and new_member[1] >7:
            categorization.append('Senior')
        else:
            categorization.append('Open')
    return categorization
    
print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))

