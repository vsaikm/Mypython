#a gaming company has players --
class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self,name,age) :
        self.name = name#attributes
        self.age = age
        
    def shout(self) :
        print(f' my name is  {self.name}')


player1 = PlayerCharacter('sai',24)

player2 = PlayerCharacter('mohan',24)
print(player1.name,player1.age)
print(player2.name,player2.age)
print(player2.membership)
print(player2.shout())


#__init__ method is a special ,this is called a dunder method or magic method ,when  we are building a class we usaully see this at the top this is constructor method or init method ....,this is utomatically called  anytime when we instantiate (whenever we are calling the class ,the code block runs )
#what ever after self is a paarameter,so we need to give the name of the character
#what is the self keywrd,,self refers to the player character that we  are going to create a player1 object 
#self is a default parameter
#self is a refernce for the object that hasnt been created(self refers to whatever to the left of the dot)
#when we instantiate ,the player1 should get name
#use same piece of code ,but hvee differnt names
#differnt players with different attributes
#DRY
#name and age are ttributes or properties this player1 object has
#print(player1) and players 2  we  get the objects are created at differnt locations
#help(list)
#=======================================

#self for progrma dynamic or cod dynamic
#class object attribute - this is static - all objects will have access to it





