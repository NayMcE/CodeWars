"""
Challenge 1 is to complete the terminal input for price 
calculations for our OdemaxCiniVue customers.

The rules are:
Custom Exceptions/ Validation:
- Children under 3 years old are not permitted into the Cinema.
- No one can earn negative money a year.
Logic:
- Children aged 3 to 12 receive the Child Discount.
- Pensioners receive a special discount.
- If a user earns less than £12,500 a year, and is not a child 
or a pensioner, they are entitled to a free ticket.

"""

##########################################
# CONSTANT VALUES FOR OdemaxCiniVue Cinema
# Prices are in pence...
PRICE_PER_TICKET = 1780
CHILD_DISCOUNT_PERCENTAGE = 50
PENSIONER_DISCOUNT_PERCENTAGE = 45
PENSIONER_AGE_CUTOFF = 65
##########################################

## Welcome Screen ########################
print("Welcome to the OdemaxCiniVue Cinema!")
print("Discounts are available at the moment...")
users_age = int(input("How old is the viewer?"))
users_wage = int(input("How much does the viewer earn a year?"))              
##########################################

"""
👇   Finish the application  👇
"""


class UnderAgeUser(Exception):
    pass

class NegativeIncomeException(Exception):
    pass

if users_wage < 0:
    raise NegativeIncomeException('Income input negative value')

if users_age < 3:
    raise UnderAgeUser('Children under 3 cannot enter the cinema')

ticket_price = 0

if users_age >= 3 and users_age < 12:
    ticket_price = PRICE_PER_TICKET * ((100 - CHILD_DISCOUNT_PERCENTAGE) / 100)
elif users_age > PENSIONER_AGE_CUTOFF:
    ticket_price = PRICE_PER_TICKET * ((100 - PENSIONER_DISCOUNT_PERCENTAGE) / 100)
elif users_wage > 12500:
    ticket_price = PRICE_PER_TICKET

print(f'Ticket price is: £{round(ticket_price / 100, 2):.2f}')
