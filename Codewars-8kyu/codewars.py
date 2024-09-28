# def greet(name, owner):
#     owner = True
#     if owner:
#         print("Hello boss")
#     else:
#         print("hello guest")


# function to calculate BMI
def bmi(weight, height):
    bmi = weight/height ** 2
    if bmi >= 0:
        if bmi <= 18.5:
            print('Underweight')
        elif bmi <= 25.0:
            print('Normal')
        elif bmi <= 30.0:
            print('Overweight')
        else: 
            print('Obese')
    else:
        print('Please enter valid details')
    return bmi

print(bmi(80, 1.80))

# # removing spaces from strings
def no_space(x):
    translation_table = str.maketrans('','',' ')
    string_without_spaces = x.translate(translation_table)
    return string_without_spaces

print(no_space('H e l l o'))

#function that greets the world
def hello_world():
    print('Hello World')

print(hello_world())    

#function that returns a string from a boolean
def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    elif boolean == False:
        return 'No'
    
print(bool_to_word(True))

#method to use additive inverse on a number given
def opposite(number):
    return number * -1

print(opposite(3))

# find either the area or perimeter of a shape
def area_or_perimeter(l, w):
    area = l * w
    perimeter = 2 * (l+w)
    if l == w:
        return area
    else:
        return perimeter
    
print(area_or_perimeter(3, 3))