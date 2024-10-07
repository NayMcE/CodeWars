# def sc(n: int) -> str:
#     str = 'Aa~ ' * n + 'Pa!'
#     # new_str = ' '.join(multiplied_str.split()[:1])
#     if n <= 1:
#         return '', 'Mans safe!'
#     elif n <= 6:
#         return multiplied_str + ' Pa! Aa!'
#     else:
#         return multiplied_str + ' Pa!'
        
    
# print (sc(6))


# def sc(n: int) -> str:
#     str = 'Aa~ ' * n
#     end_str = 'Pa!'
#     new_str = ' '.join(str.split()[:-1] + [end_str])
#     if n <= 1:
#         return '', 'Mans safe!'
#     elif n <= 6:
#         return new_str + ' Aa!'
#     else:
#         return new_str
    

# print(sc(6))

def sc(n: int) -> str:
    if n <=1:
        return ""
    if n <=6:
        return 'Aa~ ' * (n-1) + 'Pa! Aa!'
    else:
        return 'Aa~ ' * (n-1) + 'Pa!'





