#Users

#object introspection
class User(object) :
    def __init__(self, email):
        self.email = email
    def sign_in(self) :
        print('logged in :')
        
class Wizard(User) :
    def __init__(self, name, power, email) :
        #User.__init__(self, email) #this is the point(we called the init method in the user class inside the  Wizard class)
        super().__init__(email)  #claas above the wizard is super 
        self.name = name
        self.power = power
        

    def attack(self) :
        print(f'attacking with the power of {self.power}')


wizard1 = Wizard('sai' ,50, 'sai@gmail.com' )
print(dir(wizard1))

#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']

#thse are dundder methods oor magic methods
# these were inherited from base class object







 




    
    
