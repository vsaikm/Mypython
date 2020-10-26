import re


pattern = re.compile('this')
string = "search this inside of this text please"

#print(re.search('this',string))
#instead of abov command use pattern and chagne as below
a= pattern.search(string)
b= pattern.findall(string)
c= pattern.fullmatch(string)
d= pattern.match(string)

print(a)
print(b)
print(c)
print(d)



#<re.Match object; span=(17, 21), match='this'>
#a.start
#a.and
#a.group
#regx101 website
#email validation


