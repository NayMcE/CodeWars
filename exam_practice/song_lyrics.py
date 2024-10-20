file_read = open ('C:\\Users\\naomi\\Documents\\CFG_Software_Engineering_Degree_Files\\Practice\\exam_practice\\lyrics.txt', 'r') 

def lines():
    lines = file_read.readlines()
    
    for l in lines:
        if 'sing' in l:
            print(l)


print(lines())

