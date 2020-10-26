#Decorators
#function with in an other function
#starts with @ ex:@staticmethod,@classmethod




from time import time #modules (in reduce section we used different one)
def performance(fn): 
    def wrapper(*args, **kwargs) :
            t1 = time()
            print(t1)
            result = fn(*args,**kwargs)
            print(result)
            t2 = time()
            print(t2)
            print(f'took {t2-t1}  ms')
            return result
    return wrapper
        

@performance
def long_time():
    for i in range(10):
        i*5

long_time()


#read decorators

