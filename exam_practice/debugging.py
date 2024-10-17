egg_boxes = 4
eggs_per_box = 8
total_eggs = egg_boxes * eggs_per_box
message = 'I have {} eggs'.format(total_eggs) 
print(message)

# eggs_per_box was a string and not an integar so the multiplication was to the string not the integar. 
#to fix the problem we remove the quotation marks to make it an integar and the code then works.