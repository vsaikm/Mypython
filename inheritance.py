#Users
class User() :
    def sign_in(self) :
        print('logged in :')
        
class Wizard(User) :
    def __init__(self, name, power) :
        self.name = name
        self.power = power

    def attack(self) :
        print(f'attacking with the power of {self.power}')

class Archer(User) :
    def __init__(self, name, num_arrows) :
        self.name = name
        self.num_arrows = num_arrows

    def attack(self) :
        print(f'attacking with the arrows :arrows left - {self.num_arrows}') 


wizard1 = Wizard('sai' ,50)
archer1 = Archer('mohan' ,30)
print(wizard1.sign_in())
print(wizard1.attack())


print(archer1.attack())

#inheritanc 2 nd part --
print(isinstance(wizard1,User))
print(isinstance(wizard1,Wizard))
print(isinstance(wizard1,object))#object is root class



 




    
    
