# polymorphism means many forms it allowes method to have a same name but bahave differntly to based on a context 

'''overLoading and overRiding'''

'''1.Over loading 
        a.Operator Over loading 
        B.Method Over loading
'''

# #Operatoe overriding
# # ----------------------------------------
# class book:
#     def __init__(self,bname,pages):
#         self.name=bname
#         self.pages=pages
    
#     def __add__(self,other):           #__add__ speatial method 
#         return self.pages+other.pages
    
# # print(dir(b1))
    
# b1=book('book1',500)
# b2=book('book2',400)

# print(b1+b2)

# print(b1.__add__(b2))

# # -----------------------------------------

# class Hotel:
#     def __init__(self,hname,ren):
#         self.name=hname
#         self.rent=ren
    
#     def __gt__(self,other):
#         return self.rent>other.rent
    
# # print(dir(h1))
    
# h1=Hotel('taj',5000)
# h2=Hotel('raj',2000)

# print(h1>h2)

# print(h1.__gt__(h2))

##---------------------------------------------

class book:
    def __init__(self,bname,pages):
        self.name=bname
        self.pages=pages
    
    def __add__(self,other):           #__add__ speatial method 
        total= self.pages+other.pages
        return book('x',total)
    
    def __str__(self):
        return str(self.pages)
    
# print(dir(b1))
    
b1=book('book1',500)
b2=book('book2',400)
b3=book('book3',600)
b4=book('book4',500)

print(b1+b2+b3+b4)

print(b3+b4)

#----------------------------------------------------------------

# METHOD OVERLOADING 

# class calci:

#     @staticmethod
#     def sum(n1,n2):
#         return n1+n2
    
#     @staticmethod
#     def sum(float n1, float n2):
#         return float n1 + float n2


#=====================================================================================================


'''
Over-Riding


'''

class parent:
    course='java'
    def property(self):
        print("farm gold home")
    def marry(self):
        print('RelativesGirl')

class child(parent):
    course='python'
    def myproperty(self):
        print("flat car")
    def marry(self):
        print('xyz')

c=child()
p=parent()
print(c.course)
print(c.marry())

#------------------------------------------------------------------

class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.bredth=b

    def area(self):
        return self.length * self.bredth
    
    def perimeter(self):
        return 2*(self.length + self.bredth)
    
r1=rectangle(10,5)
r2=rectangle(20,10)

print(r1.area())
print(r2.perimeter())

#---------------------------------------------------------------------

class square(rectangle):
    def __init__(self,side):
        self.side=side

    # def area(self):
    #     return self.side**2
    
    # def perimeter(self):
    #     return 2*(self.side)
    
s1=square(10)
s2=square(20)

print(s1.area())
print(s2.perimeter())





        