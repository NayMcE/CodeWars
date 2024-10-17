
    #Move every letter in the provided string forward 10 letters through the alphabet.
    # If it goes past 'z', start again at 'a'.
    # Input will be a string with length > 0.
    
def move_ten(st):
    my_string  = st
    difference = 10
    new_string = ''.join((chr(97+(ord(letter)-97+difference) % 26) for letter in my_string))
    return new_string

    
    
    #     test.assert_equals(move_ten("codewars"), "mynogkbc")
    #     test.assert_equals(move_ten("exampletesthere"), "ohkwzvodocdrobo")
    #     test.assert_equals(move_ten("returnofthespacecamel"), "bodebxypdroczkmomkwov") 
    #     test.assert_equals(move_ten("bringonthebootcamp"), "lbsxqyxdrolyydmkwz") 
    #     test.assert_equals(move_ten("weneedanofficedog"), "goxoonkxyppsmonyq") 


print(move_ten('codewars'))