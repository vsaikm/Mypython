#print(1 + True)
#print(1 + 'hello')

#error handling
#def hooooo():
#    1 + name

#hooooo()#NameError: name 'name' is not defined

while True:

    try :
        age = int(input('what is your age?'))
        10/age
        
    except ValueError:
        print('Please enter the numebr')

    except ZeroDivisionError:
        print('Please enter the numebr other than 0')

    else:
        print('thank you!!!')
        break
        
    
