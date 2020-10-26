#lambdaexpressions
my_list = [1,2,3]

    
def accumulator(acc, item):
    print(acc, item)
    return acc + item
print(list(map(lambda item : item*2, my_list)))
print(list(filter(lambda item : item % 2, my_list)))
#print(reduce(lambda acc,item : acc + item, my_list))

print(list(map(lambda item : item**2, my_list)))

#lambda expressions excercise:



