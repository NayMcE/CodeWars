def mouth_size(animal): 
    animal = animal.lower()
    if animal == 'alligator':
        return 'small'
    else:
        return 'wide'
    
print(mouth_size('alliGATOR'))