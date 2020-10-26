#create a super list using the class super list
class SuperList(list):#we use list here 
    def __len__(self):
        return 1000
        
super_list1 =  SuperList();


print(len(super_list1))
super_list1.append(5)#append
print(super_list1[0])

print(issubclass(SuperList, list)) #list is a super class of SuperList 
print(issubclass(list, object))#object  is super clas of list



#after this  130 and 131 chapters
