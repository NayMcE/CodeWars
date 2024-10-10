def xo(s):
    x = sum(c in 'x' for c in s.lower())
    o = sum(c in 'o' for c in s.lower())
    if x == o:
        return True
    else:
        return False 
    

print(xo('zpzpzpp'))


# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

