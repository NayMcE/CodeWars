# def count_sheeps(sheep):
#     return sum([1 for s in sheep if s])

# print(count_sheeps([True, True, False, True]))


def can_pay(price, cash_given):
    if cash_given >= price:
        return True
    else:
        return False


print(can_pay(100, 250))