#collections module from python module index website
from collections import Counter,defaultdict, OrderedDict #here there are classes and one function


'''li = [1,2,3,4,5,7,7,8,8,8]
print(Counter(li))
#op:Counter({8: 3, 7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
sentence = 'venkata sai kumar'
print(Counter(sentence))
#Counter({'a': 4, 'k': 2, ' ': 2, 'v': 1, 'e': 1, 'n': 1, 't': 1, 's': 1, 'i': 1, 'u': 1, 'm': 1, 'r': 1})
#turning a list into hasmap is very useful in  optimisation problems
#want to count duplicate users and duplicate emails counter is useful
'''
'''
dictionary =  defaultdict(int,{'a' : 1, 'b' : 2})#we need to give a callable object as a first argument ,if we give int 0 is the output #cllable means the functio thst can be run
#we can give lambda :'doesnt exist ' like that 
print(dictionary['a'])
print(dictionary['c'])
'''
'''
d = OrderedDict()
d['a'] =1
d['b'] =2

d2 = OrderedDict()
d2['a'] =1
d2['b'] =2

print(d2==d)#True
#when we change the order then the answerr is false'''
#we can just use regular dictionaries






