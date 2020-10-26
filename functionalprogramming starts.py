#Separatin oof cencerns,packing our code into separate chunks, separate data and functions
#have an emphasis of data
#goal is same as oop
#easy t extend
#DRY
#pure functions
#============================

#def multiply_by2(li):
#    new_list = []
#    for item in li:
#        new_list.append(item*2)

#    return new_list

#print(multiply_by2([1,2,3]))

#==============================
wizard = { #separate the data and functions 
    'name' : 'Merlin',
    'power' : 40
    }

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)

    return new_list

print(multiply_by2([1,2,3]))  # a pure func doesnt have sid effects (interacts outside the function)
#we can easily understand the code


