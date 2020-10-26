#filtering the reults

my_list = ['sai', 'alex','amar','boo']
def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, my_list)))#instead of map keep filter 
print(my_list)

=================================================== RESTART: C:/Users/sai kumar mullapudi/Documents/python/filter.py ==================================================
[1, 3]
[1, 2, 3]
#we have list of users we gotta need tofilter out hte users startig with letter 'A'
