#debugging -- removing the errors from code

#linting :allows us to detecct as we code

        #num +4

#IDES and editors

#Pbd - python debugger
#it is a builtin  module

import pdb
def add(num1,num2):
    pdb.set_trace()
    t = 4 * 5#interactive python debuuger in the python console 
    return num1 + num2 


add(4,5)

#> c:\users\sai kumar mullapudi\documents\python\section 12,, debugging in python\how to debug code.py(15)add()
#-> return num1 + num2
#(Pdb) 4Counter({'a': 4, 'k': 2, ' ': 2, 'v': 1, 'e': 1, 'n': 1, 't': 1, 's': 1, 'i': 1, 'u': 1, 'm': 1, 'r': 1})
#*** SyntaxError: invalid syntax
#(Pdb) num1
#4
#(Pdb) num2
#5
#(Pdb)

#practice one example with pdb


