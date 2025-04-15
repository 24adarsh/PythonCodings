#Operators
# 1.Arithmetic(+-)
# 2.logical
# 3.assignment
# 4.comparison/relational
# 5.

# ARITHMETIC OPERATOR 

# ADD +
n1=10
n2=20
print(n1+n2)  #30

s1='hari'
s2='om'
print(s1+s2) #hariom

l1=[11,22]
l2=[33,44]
print(l1+l2)  #[11, 22, 33, 44]

t1=(1,2,3,'a','b')
t2=(4,5,6,'c','d')
print(t1+t2)  #(1, 2, 3, 'a', 'b', 4, 5, 6, 'c', 'd')

# s3={1,3,5}
# s4={2,4,6}
# print(s3+s4)  
#TypeError: unsupported operand type(s) for +: 'set' and 'set'

a=2
b=2.2
print(a+b) #4.2

# sub (-) as same as addition 

#mul *

# /   =>float Value
# //  => int value

n1=10
n2=3
print(n1/n2)  #3.333
print(n1//n2)  #3

# % modulus => returns remainder from division

n1=10
n2=3
print(n1%n2) #1

# power ** 

print(n1**2) #100

'''COMPARISON OPERATOR'''

# =>bool 

'''
<   smaller than
>   greater than
<=  smaller than or equal to
>=  greater than or equal to
==  equal
!=  not equal
'''

'''LOGICAL OPERATOR '''

# AND 
# if both conditions are mandatory if both true it returns True
# if one is false results will be false 

# OR
# here one condition is mandatory if one codition is true it returns True
# if both is false results will be false 


# +=
num1=10
n1+=2
print(n1) #addition 12

# -=
n1-=2
print(n1)  #substraction 10

# /=
n1/=3
print(n1)  #division in float 3.3333

# //=
n2=10
n2//=3
print(n2)   #division in int 3

# SPEATIAL OPERATORS

# IN 
l=[11,22,33,44,55]
print(33 in l)  #true

d={'name':'kunal','age':45}
print('name' in d )

name= 'vaibhav'
print('r' in name)

d={'name':'kunal','age':45}
print (45 in d.values())

#is
# it checks obj id id whether same or not 

# == it checks the value is present or same

'''
INTERVIEW QUESTIONS

1. what is operator
2. what are types of operator
3. what is diff between (== and is)(/ and //)
'''







