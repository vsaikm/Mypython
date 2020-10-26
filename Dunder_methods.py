#Dunder_methods
#these wwewre  inherited from base obj class
class Toy():
    def __init__(self, color, age): #define a toy and initialize it with color and age
        self.color = color
        self.age = age
        self.my_dict ={
            'name' : 'yoyo' ,
            'has_pets' : False 
            
            }

    def __str__(self):
        return f'{self.color}'  #not to modify the dunder methds

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted:')

    def __call__(self):
        return('Yes')

    def __getitem__(self, i):
        return self.my_dict[i]
        



#we want to create action figure

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(len(action_figure))  #we modifies the length dunder method

print(str(action_figure)) #both are same

print(action_figure()) #call dunder method prints yes in the console

print(action_figure['name'])
print(action_figure['has_pets'])
        
