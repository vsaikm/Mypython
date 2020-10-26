#scope - wahat variables do i have access to?

total = 0
def count(total):
    total += 1
    return total
    
print(count(count(count(total))))

#1 - start with local
#2 - pareent local?
#3 -global
#4 - built in python functions

