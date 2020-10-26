#a gaming company has players --
class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self,name='anonymous',age=0) :
        if (age > 18):
            print("the age must be  greateer than  18")
            self.name = name#attributes
            self.age = age
        
    def shout(self) :
        print(f' my name is  {self.name}')
        return done


player1 = PlayerCharacter('sai',18)

print(player1.shout())
