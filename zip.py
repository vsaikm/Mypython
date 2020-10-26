my_list = ['sai', 'alex','amar','boo']
def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0

print(list(filter(multiply_by2, my_list)))#instead of map keep filter 
print(my_list)
