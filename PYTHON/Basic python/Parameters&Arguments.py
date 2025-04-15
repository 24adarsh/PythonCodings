'''parameters and arguments

parameters -- these are variables which is defined in fumction statement

arguments -- these are values which are declared for variables in function

'''

# def cube (num):
#     return num**3

# print(cube(5))


# def details(name,age, city): 
#     return f'my name is {name} i am {age} year Old and i am from {city}' 

# print(details('vaibhav patil', 25, 'pune'))


'''keyword argument

def fun(p1,p2): 
    pass


fun(p1=v1,p2=v2) 
fun(p2=v2,p1=v1)
'''

# def details(name,age,city): 
#     return f'my name is {name} i am {age} year old and i am from {city}' 
# print(details(25, 'pune', 'vaibhav patil'))     #here order is nessesry
# print(details(age=25,city='pune', name = 'vaibhav patil'))   #order is not nssery


# def details(name,age,city, inst='TΚΑ'): 
#     return f'my name is {name} i am {age} year old and i am from {city}  institute name is {inst}' 

# print(details('vaibhav patil',25, 'pune' inst='Java by kiran'))
# print(details(age=25,city='pune', name ='kunal patil')) 

# num=int(input('enter a number: '))
# def even():
#     if num%2==0:
#         print(f'{num} is even')
#     else:
#         print(f'{num} is odd')
# even()

'''lamda function

'''

# def add(n1,n2):
#     sum=n1+n2
#     return sum
# print(add())

# lambda arg: expression

# add=lambda n1,n2: n1+n2
# print(add(1,2))

# def sq(num):
#     square=num**2
#     return square
# print(sq(3))

# sq=lambda num: num**2
# print(sq(3))

# print((lambda num: num**2)(4))            #lambda func can be done in one 

# calci=lambda n1,n2: (n1+n2,n1*n2,n1-n2,n1/n2)
# print(calci(20,10))

'''nested lambda'''

# def f1(n1):
#     def f2(n2):
#         return n1+n2
#     return f2
# f2=f1(2)
# print(f2(3))

# add1 = lambda n1: lambda n2:  n1+n2
# add2= add1(3)
# print(add2(7))

# add1 = lambda n1: lambda n2:  n1+n2
# print(add1(2)(3))

'''Higher order functions'''

# numbers=[1,2,3,4,5,6,7,8]
# def even(iterable):
#     num=0
#     if num in iterable:
#         num%2==0
#         return True
# print(list(filter(even,numbers))) ###############

# numbers=[1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda num: num%3==0,numbers)))

student=['rajesh','ajay','rahul','sujay','ram','rakshak']
# print(list(filter(lambda name: name.startswith('r') ,student)))

# print(list(filter(lambda name: name[0]=='r' ,student)))
print(list(filter(lambda name: name.endswith('jay') ,student)))


result={'aditya':50,'divya':91,'ganesh':43,'vaishnavi':32}
# filter names of student passed
print(list(filter(lambda name: result[name]>75 ,result)))
print(dict(filter(lambda t: t[1]>75 ,result.items())))  #t is tuple

emp={'aditya':50000,'divya':91000,'ganesh':51000,'vaishnavi':32000,'rahul':62000}
# print employee details in dict who has sallary between 50-65k
print(dict(filter(lambda r: r[1]>65000 &  r[1]>50000,emp.items())))

voters={'aditya':50,'divya':17,'ganesh':43,'vaishnavi':32}
# print dict of voters who can vote 
print(dict(filter(lambda s: s[1]>18 ,voters.items())))














