def can_afford(cost):
    petty_change = {0.01: 6, 0.02: 4, 0.05: 7, 0.1: 6, 0.2: 4, 0.5: 10, 1.0: 6, 2.0: 2}
    # add together the petty change to see how much they have in their pocket
    sum_petty_change = {key: key * value for key, value in petty_change.items()}
    new_dict = 
    if sum_petty_change > cost:
        return 'can afford it'
    else:
        return 'cant afford it'