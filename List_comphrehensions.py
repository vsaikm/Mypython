#List,set,dictionary comphrehensions are there in python which are unique

my_list = [char for char in 'hello']
print(my_list)


my_list1 = [i for i in range(1,100)]
print(my_list1)

my_list1 = [i*2 for i in range(1,100)]
print(my_list1)

my_list1 = [i**2  for i in range(1,100)]
print(my_list1)

my_list1 = [i for i in range(1,100)
            if i % 2 ==0]
print(my_list1)
