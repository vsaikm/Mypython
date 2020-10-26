#a gaming company has players --
class PlayerCharacter:
    def __init__(self,name,age) :
        self.name = name#attributes
        self.age = age
        
    def run(self) :
        print('run')
        
    def speak(self) :
        print(f'my name is {self.name} , and  i am {self.age} years old')
        

player1 = PlayerCharacter('sai',23)
print((1,2,3,4,4).count(4))

#player3 = PlayerCharacter.adding_things(


#print(player1)

#print(player1.adding_things(2,3)) #op is 5



