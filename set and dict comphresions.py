#for set comphrehensions keep [] with {} brackets
#htat is for set
simple_dict = {
    'a' : 1,
    'b' : 2
    }

my_dict = {key:value*2 for key,value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict1 = {num:num*2 for num in [1, 2, 3]}
print(my_dict1)


op:
    {'b': 4}
{1: 2, 2: 4, 3: 6}
