'''OOP
class:
Object:
Ref Variable:

'''

# class
# -------------
# blueprint=>object
# object=>attribute and methods
# class contains multiple objects
# class doesnt requires memory 
# it is a imaginary entity
# first letter is capital



# object
# --------------
# object is a instance of classit 
# it is physical entity
# object requires memory execution


# ref variable
#---------------------
# it refers the class objects 
# it is used to access functionality of object



# SYNTAX====

# class Class_name:
#     attributes and method

# ref_variable1=Class_name()
# ref_variable1=Class_name()
# ref_variable1=Class_name()



# if function is inside the class it is called as method 
# if function is outside the class it is called as function


# class Xyz:
#     def __init__(self):                       #__init__ is a speatial method 
#         print(f'id of self is {id(self)}')
# x1=Xyz() 
# print(f'id of x1 is {id(x1)}')
# x2=Xyz()
# print(f'id of x2 is {id(x2)}')

# when object is called with ref_variable it assigns argument value to self automatically 

class Student:
    def __init__(self,nm,ag,ct):
        self.name=nm
        self.age=ag
        self.city=ct
s1=Student('akshay',23,'pune')
s2=Student('abhay',25,'pune')

class Emp:
    company_name='TCS'
    def __init__(self,nm,id,dept,sal,ct):
        self.name=nm
        self.id=id                    #constructor
        self.department=dept          #constructor doesn't returns any value
        self.sallary=sal
        self.city=ct
        print(self.name,self.id,self.department,self.sallary,self.city)
e1=Emp('yash',101,'electrical',21000,'pune')
e2=Emp('raj',102,'machanical',21000,'pune')
e1.sallary=25000
print(e1.sallary)
print(e1.company_name)


class Mobile:
    brand_name='xiomi'
    def __init__(self,nm,mdl,ram,rom,clr):
        self.name=nm
        self.model=mdl
        self.ram=ram
        self.rom=rom
        self.colour=clr
m1=Mobile('redmi ','note 9 pro',6,128,'blue')


''''06-02-2025

METHODs

1.Instance Method
2.Class Method
3.Static Method
'''

# -----------------------------
# Instance method = instance variable
# def IM(self)
#     Instance variable operations

# by using ref variable

# ---------------------------------
# class method=>class variable 
# @classmethod
# def CM(cls):
#     #class variable

# by using class name

# ------------------------------------
# static method => local variable 

# @staticmethod 
# def SM (p1,p2):
#     #local variable 

# by using class name 

# --------------------------------------


# class Bank:
#     Bank_name='SBI'
#     print('customer details')
#     def __init__(self,nm,actype,Acnum,Adhar):
#         self.name=nm
#         self.account_type=actype
#         self.Account_number=Acnum
#         self.Adhar_num=Adhar
# b1=Bank('pruthvi','savings',634363735,'1282 2223 3455')

"""-----------------------------------------------------------------------------------"""

class Student:
    institute_name='TheKiranacademy'
    coure='python'
    trainer='vaibhav patil'
    fee=40000
    def __init__(self,nm,ag,ct):     #Class method
        self.name=nm
        self.age=ag
        self.city=ct
        self.mrk={}

    def details(self):               #instance Method
        return f'''
            Name : {self.name}
            City : {self.city}
            Age : {self.age}
            institute_name : {Student.institute_name}
            course : {Student.coure}
            trainer : {Student.trainer}
        -------------------------------------------------
            '''
    
    def add_marks(self,mar,hindi,eng,math,sci):    #local method
        self.mrk[mar]=mar
        self.mrk[hindi]=hindi
        self.mrk[eng]=eng
        self.mrk[math]=math
        self.mrk[sci]=sci
        return 'added'
    
    def cal_percentage(self):
        ob=0
        for mark in self.mrk.values():
            ob=ob+mark
        per=(ob/500)*100
        return '%.2f'%per +' %'
    
    @classmethod
    def inst_details(cls):
        return f'''
        institute name: {cls.institute_name}
        course        : {cls.coure}
        trainer name  : {cls.trainer}
        '''
    @classmethod
    def Main_fees(cls,dis):
        mf=cls.fee-cls.fee*(dis/100)
        return mf



s1=Student('Akshay',28,'bombay')
s2=Student('Abhay',25,'pune')

print(s1.details())
print(s2.details())

print(s1.add_marks(50,60,70,80,90))
print(s1.cal_percentage())

print(s2.add_marks(90,60,70,80,90))
print(s2.cal_percentage())

print(Student.inst_details())

print(Student.Main_fees(12))   # used classs method

# ------------------------------------------------------------------------------  
# ------------------------------------------------------------------------------  
# ------------------------------------------------------------------------------  

'''7-2-25'''
'''
questions :

what is static method 
diff between self and cls
define class method
diff between class andd object ??
'''


'''
STATIC METHODS
@staticmethod
def sm(11,12):
   pass
   


'''
class Bank_cust:
    Bank_name='SBI'
    Ifsc_code= 'SBIN00678'
    Branch = 'Karve Nagar'
    def __init__(self,nm,actype,Acnum,Adhar,mob,pan,bal):
        self.name=nm
        self.account_type=actype
        self.Account_number=Acnum
        self.Adhar_num=Adhar
        self.Mob_no=mob
        self.PAN=pan
        self.Balence=bal

    def Show_details(self):
        return f'''
           name           : {self.name}
           account number : { self.Account_number}
           account type   : { self.account_type}
           adhar number   : { self.Adhar_num}
           mobile number  : { self.Mob_no}
           PAN number     : { self.PAN}
           Ac Balence     : { self.Balence}       
         '''

    def deposit(self,amount):
        self.Balence=self.Balence+amount
        return 'done'

    def withdraw(self,amount):
        self.Balence=self.Balence-amount
        return 'done'
    
    # def trasfer(self,amount,to_transferAccNumber):
    #     if self.Account_numb ==
    
    @staticmethod
    def si(amount,per,t):
        simple=(amount*(per)*t)/100
        return simple
    
    @staticmethod
    def ci(amount,per,n,t):
        compound=amount+(1+per/100*n)**(n*t)
        return compound
    
c1=Bank_cust('pruthvi','savings',634363735,'1282 2223 3455',8558550234,'DFR2344',500000)
c1=Bank_cust('pratik','savings',234363735,'1212 2223 3455',8558234234,'ABC2344',660000)

print(c1.Show_details())

print(c1.deposit(5000))

print(c1.Show_details())

print(c1.withdraw(2000))

print(c1.Show_details())

print(Bank_cust.si(1000,10,3))

print(Bank_cust.ci(1000,10,1,3))










