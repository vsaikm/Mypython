#Files I/O
#input something from outside world and output something into the outside world
my_file = open('test.txt')
print(my_file.readlines())
#open function has the idea of the cursor 
#op:<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>

#['Hi my name is sai\n', 'Hi my name is sai\n', 'Hi my name is sai\n', 'Hi my name is sai\n', 'Hi my name is sai\n', ':)']
my_file.close()
