def reverse_words(s):  
# input string
# reversing words in a given string
    s = s.split()[::-1]
    l = []
    for i in s:
# appending reversed words to l
        l.append(i)
# printing reverse words
    return(" ".join(l))

print(reverse_words('Hello world'))