petty_change = {0.01: 6, 0.02: 4,
0.05: 7, 0.10: 6, 0.20: 4, 0.50:
10, 1.00: 6, 2.00: 2}
payment_method = petty_change.fromkeys(petty_change, 0)

def pay_with_coins(money):
    paid = False
    biggest_coin_index = -1
    while not paid:
        if money == 0: return payment_method coin =list(petty_change.keys())[biggest_coin_index]
    if money >= coin and petty_change[coin] > 0:money = round(money -coin, 2)
    petty_change[coin] -= 1
    payment_method[coin] += 1
    else: 
    if biggest_coin_index > -8:biggest_coin_index -= 1
    else: return("Can't afford this with the available petty change")