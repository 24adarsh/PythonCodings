'''ENCAPSULATION
Encapsulation in python is achived by restricting direct acces to class variables and allowing modifications only to getter and setter methods 
it implemented using single underscore and double underscore for private variables and getter and setter methods to acces private method 

to make variable add 2 underscore infront of it

'''

# class Counter:

#     def __init__(self):
#         #self.count=0       anybody can access it
#         self.__count=0      #private variable 

#     def inc(self):
#         self.__count+=1
    
#     def dec(self):
#         self.__count-=1
    
#     def check(self):
#         return self.__count

# obj=Counter()

# obj.inc()
# print(obj.check())

# obj.inc()
# obj.inc()
# print(obj.check())

# obj.dec()
# print(obj.check())

# obj.count=345      
# obj.__count=456
# print(obj.check())

# #==============================================================================

# 'GETTER & SETTER METHODS'

# class Student:
#     def __init__(self,nm,ag):
#         self.__name=nm 
#         self.__age=ag  
#     def get_name(self):
#         return self.__name
#     def set_name(self,un):
#         if isinstance(un,str) and un.isalpha():     #putting a validation terms
#             self.__name=un
#     def get_age(self):
#         return self.__age
#     def set_age(self,ua):
#         if isinstance(ua,int) and ua>0:    #putting a validation terms
#             self.__name=ua

        
# s1=Student('om',23)
# s2=Student('riya',22)

# print(s2.get_name())

# s1.set_name('1234')
# print(s1.get_name())

# s1.set_age(25)
# print(s1.get_age())   

# s1.set_name('pruthvi')
# print(s1.get_name())   

# s1.set_age(-21)
# print(s1.get_age())   #doesnt takes nagetive values

# s1.set_name('1234')
# print(s1.get_name())   #doesnt takes a int values

# s1.set_age(27)
# print(s1.get_age())

#====================================================================


# class Student:
#     def __init__(self,nm,ag):
#         self.__name=nm 
#         self.__age=ag

#     @property                             #it makes use function as variable doesnt need to call function ()
#     def get_name(self):
#         return self.__name
#     @get_name.setter                      #adding or joining getter and setter methods
#     def set_name(self,un):
#         if isinstance(un,str) and un.isalpha():     
#             self.__name=un

#     @property
#     def get_age(self):
#         return self.__age
#     @get_age.setter
#     def set_age(self,ua):
#         if isinstance(ua,int) and ua>0:    
#             self.__name=ua

        
# s1=Student('om',23)
# s2=Student('riya',22)

# print(s2.get_name)

# s1.set_age=25
# print(s1.get_age)   

# s1.set_name='pruthvi'
# print(s1.get_name)   

# s1.set_age=27
# print(s1.get_age)   

#=================================================================

class Employee:
    def __init__(self,nm,sal,jd):
        self.name=nm
        self.__salary=sal
        self.__joing_date=jd
        self.last=jd


        




