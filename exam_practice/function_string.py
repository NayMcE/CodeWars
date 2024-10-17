# Write a function that takes in a string, and prints out the following:
# ● The string in uppercase
# ● The string in lowercase
# ● Whether the word starts with the same letter as the last letter ● The string
# with all instances of the first letter replaced with “[REDACTED]”

def string_changes(str):
    print(str.upper())
    print(str.lower())
    if str[0] == str[-1]: 
        str.replace('', "REDACTED")        


print(string_changes('abcda'))

# Function to process a given string as per the requirements
def process_string(s):
    # Uppercase version of the string
    print("Uppercase:", s.upper())
    
    # Lowercase version of the string
    print("Lowercase:", s.lower())
    
    # Check if the string starts and ends with the same letter
    if s[0].lower() == s[-1].lower():
        print("The string starts and ends with the same letter.")
    else:
        print("The string does not start and end with the same letter.")
    
    # Replace all instances of the first letter with "[REDACTED]"
    first_letter = s[0]
    redacted_string = s.replace(first_letter, "[REDACTED]")
    print("Redacted string:", redacted_string)

# Example usage
process_string("racecar")
