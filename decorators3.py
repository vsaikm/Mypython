#Decorators
#function with in an other function
#starts with @ ex:@staticmethod,@classmethod
def my_decorator(func):#higher order function
    def wrap_func(*args, **kwargs):
        print('******************')
        func(*args, **kwargs)
        print('******************')
    return wrap_func

@my_decorator
def hello(greeting , emoji = ':('):
    print(greeting, emoji)

a = my_decorator(hello)
a('hii', ':)')

#op:
#******************
#helloooooooooooooo
#******************
#enhances the function

