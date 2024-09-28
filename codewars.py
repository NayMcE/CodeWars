# def greet(name, owner):
#     owner = True
#     if owner:
#         print("Hello boss")
#     else:
#         print("hello guest")

# 
# 
# def bmi(weight, height):
#     bmi = weight/height ** 2
#     if bmi >= 0:
#         if bmi <= 18.5:
#             print('Underweight')
#         elif bmi <= 25.0:
#             print('Normal')
#         elif bmi <= 30.0:
#             print('Overweight')
#         else: 
#             print('Obese')
#     else:
#         print('Please enter valid details')
#     return bmi

# print(bmi(80, 1.80))

def no_space(x):
    translation_table = str.maketrans('','',' ')
    string_without_spaces = x.translate(translation_table)
    return string_without_spaces

print(no_space('H e l l o'))

