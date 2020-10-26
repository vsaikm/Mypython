#Generators: generate sequence of values
#range() is a generator
#special keyword - yield
def make_list(num):
    result= []
    for i in range(num):#range is a generator
        result.append(i*2)
    return result

my_list = make_list(100)
#print(my_list)

#it is taking up space
print(list(range(100000)))


#iterable - any object in python whihc were able to loop through underneath the hood it has dunder method
#__iter__ - so when the object is created this iter allow us to have an iterable object that can be iterated over to iterate something
#generators - but not evrything that is iterable is not a generator 

#list is iterable but not a genertor
