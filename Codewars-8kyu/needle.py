def find_needle(haystack):
    index_of_needle = haystack.index('needle')
    return(f'found the needle at position {index_of_needle}')
    
    
    
print(find_needle(['hay', 'junk', 'hay', 'needle']))

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'