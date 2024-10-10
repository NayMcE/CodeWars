# def get_count(sentence):
#     count = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for i in range(len(sentence)):
#         if sentence[i] in vowels:
#             count += 1
#     return count



def getCount(s):
    return sum(c in 'aeiou' for c in s)

print(getCount("should count all vowels"))