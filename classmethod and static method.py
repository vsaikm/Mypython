#a gaming company has players --
#decorator - 
class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self,name,age) :
        
            self.name = name#attributes
            self.age = age
        
    def shout(self) :
        print(f' my name is  {self.name}')
        return done

    @classmethod #with this decorator know we can create a function(we use whn we want to modify or change attributed)
    def adding_things(cls,num1,num2) :  #cls which means class ,we no neeed to instantiate the class 
        return cls('mohan',num1 + num2) #using cls ssstill we get output
    
    
    @staticmethod #with this decorator know we can create a function(we dnt bother about attributes here )
    def adding_things2(num1,num2) :  #wont be using cls 
        return num1 + num2 #wont be using cls 

#player1 = PlayerCharacter('sai',23)
#player3 = PlayerCharacter.adding_things(


#print(player1)

#print(player1.adding_things(2,3)) #op is 5



player3 = PlayerCharacter.adding_things(2,3) #op is 5
print(player3.age) #op is 5
