#Inheritance
class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname):
        self.name=newname
    def __str__(self):
        return "age is " + str(self.age)+" name is " +str(self.name)
myanimal=Animal(3)
print(myanimal)
a=Animal(5)
a.set_name("Kutty")
print(a)



class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname):
        self.name=newname
    def __str__(self):
        return "age is " + str(self.age)+" name is " +str(self.name)
def make_ani(l1,l2):
    l3=[]
    for i in range (len(l1)):
        a=Animal(l1[i])
        a.set_name(l2[i])
        l3.append(a)
    return l3
l1=[1,2,3]
l2=["Fluffy","Tommy","Rafiel"]
ani=make_ani(l1,l2)
for i in ani:
    print(i)

    
    
class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname):
        self.name=newname
    def __str__(self):
        return "age is " + str(self.age)+" name is " +str(self.name)  
class Cat(Animal):
    def speak(self):
        print("Meow")
    def __str__(self):
        return "animal: "+ str(self.name)+ " age: "+ str(self.age)
class Rabbit(Animal):
    tag=1
    def __init__(self,age,parent1="ATG",parent2="PTG"):
        Animal.__init__(self, age)
        self.parent1=parent1
        self.parent2=parent2
        self.rid=Rabbit.tag
        Rabbit.tag+=1
    def __str__(self):
        return "Age is "+ str(self.age)+" owners are "+ str(self.parent1)+" and "+str(self.parent2)
r1=Rabbit(8)       
r2=Rabbit(6)      
print(r1)
c=Cat(5)
c.set_name("Kitty")
print(c)
c.speak()
 
    
    
    
    
    




