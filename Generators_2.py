#Generators: generate sequence of values
#range() is a generator
#special keyword - yield
#def make_list(num):
#    result= []
#    for i in range(num):#range is a generator
#        result.append(i*2)
#    return result

#my_list = make_list(100)
#print(my_list)

#it is taking up space
#print(list(range(100000)))


#iterable - any object in python whihc were able to loop through underneath the hood it has dunder method
#__iter__ - so when the object is created this iter allow us to have an iterable object that can be iterated over to iterate something
#generators - but not evrything that is iterable is not a generator 

#list is iterable but not a genertor
#yield - instead of returning and appending this list and creating all this data ,
#pauses the function and comes back to it when we do something which is clled next(we only held one item inmemory)
#what does the yield keyword actually do????????
#A)
#===============================================================
def generator_function(num):
    for i in range(num):
        yield i
        
g = generator_function(1)
#Traceback (most recent call last):
#  File "C:/Users/sai kumar mullapudi/Documents/python/Generators/Generators_2.py", line 33, in <module>
#    next(g)
#StopIteration
next(g)
next(g)
print(next(g))#next can be called untill we each stopiteration
#op: <generator object generator_function at 0x04142990>

#for item in generator_function(10):
#    print(item)



