# import random

# def roll_dice(times: int):
    
#     # times_runned = 0
#     # while times_runned < times:
#     for i in int:
#         result = random.randint(1, 6) + random.randint(1, 6)
#         print(result)
#         # times_runned += 1

# roll_dice(100)

import random # IMPORTING RANDOM 

def roll_dice():
    statistics = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for i in range(100): 
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        statistics[dice1+dice2] += 1
        desired_total = int(input('What number do you wish to get? '))
        if desired_total in statistics.keys():
            print(f'the chance of you getting a {desired_total} is {statistics.get(desired_total)}%')
        else:
            print(f'the chance of you getting a {desired_total} os 0%')
        return statistics

print(roll_dice())