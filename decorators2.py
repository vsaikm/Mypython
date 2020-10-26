#Decorators
#function with in an other function
#starts with @ ex:@staticmethod,@classmethod
def my_decorator(func):#higher order function
    def wrap_func():
        print('******************')
        func()
        print('******************')
    return wrap_func

@my_decorator
def hello():
    print('helloooooooooooooo')


hello()

@my_decorator
def bye():
    print('bye')

    
bye()

#op:
#******************
#helloooooooooooooo
#******************
#enhances the function

