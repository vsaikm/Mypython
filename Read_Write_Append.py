#with open('test.txt') as my_file:
#    print(my_file.readlines())
#until this point we only read the file

#with open('test.txt',mode= 'w') as my_file:
#    text =my_file.write(':)')#this expression is added at the oth postion of the file :) are the 2 characters 
#    print(text)


with open('sad.txt',mode= 'w') as my_file:
    text =my_file.write(':(')
    print(text)
    
