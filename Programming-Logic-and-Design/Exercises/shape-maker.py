rows = int(9)
#for column in range (row):
    #if column <+ row/2:
        #print(("*" " ")*column)
    #else:
        #print(("*" " ")*(row-column))

for column in range (rows+1):
    if column < (rows+1)/2:
        for star in range(column):
            print("*",end=" ")
        print()
    else:
        for star in range((rows+1)-column):
             print("*",end=" ")
        print()

for column in range (rows+1):
    if column < rows/2:
        for space in range((rows+1)-column):
            print(" ",end=" ")
        for star in range(column):
            print("*",end=" ")
        print()
             
    else: 
        for space in range(column):
            print(" ",end=" ")
        for star in range((rows+1)-column):
             print("*",end=" ")
        print()
        
for column in range (rows+1):
    if column < (rows+1)/2:
        for star in range(column):
            print("*",end=" ")
        for space in range(rows+1-column-star-1-1):
            print(" ",end=" ")
        for star in range(column):
            print("*",end=" ")
        print()
    else:
        
        for star in range((rows-column)+1):
            print("*",end=" ")
        for space in range((column-5)): 
            column= column+1 
            print("s",end=" ")
        
       
        print()
      



    