some_list = ['a','b','b','n','n']

#duplicates= []
#for value in some_list:
#    if some_list.count(value) > 1:
#        if value not in duplicates:
#            duplicates.append(value)
#
#print(duplicates)

duplicates = list(set( [ value for value in some_list if some_list.count(value) > 1 ]))


print(duplicates)
