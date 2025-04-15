n1=int(input('num1: '))
n2=int(input('num2: '))
'''# %d => decimal'''
print('sum of', n1,'and ',n2,'is :',n1+n2)
print('sum of %d and %d is %d'%(n1,n2,n1+n2))

n1=float(input('num1: '))
n2=float(input('num2: '))
''' #%f => float'''
print('sum of', n1,'and ',n2,'is :',n1+n2)
print('sum of %f and %f is %f'%(n1,n2,n1+n2))
print('sum of %0.2f and %0.3f is %0.1f'%(n1,n2,n1+n2))

'''%s => String'''
name='kunal'
city='pune'
print('my name is %s , im from %s'%(name,city))

name=100
city=200
print('my name is %s , im from %s'%(name,city))

''' # . formaat method'''
name='kunal'
city='pune'
print('my name is {} , im from {}' .format(name,city))
'''position of place holder'''
print('my name is {} , im from {}' .format(city,name))
'''index of place holder'''
print('my name is {1} , im from {0}' .format(city,name))

print(f'my name is {name} im from {city}')


# n1=100
# n2=200
# n3=300
'''sep default value is black space ie. sep=>'''
#print(n1,n2,n3)          
# print(n1,n2,n3,sep='*')
'''end=> is \n'''
# print(n1,n2,n3,end='*')   

''' \n is used to print on next line'''

# print('hello student')
# print("hello \nstudent ")

''' \t is used to print tab 1tab = 4space '''

# print("hello\t\t student ")

# n1=100
# n2=200
# n3=300

# print(n1,end="@" "\n")
# print(n1,n2,n3,sep="  ")


#wap a program to iterate only perfect numbers

l=[10,20,6,50,7,28,476,96,8128,9]
for num in l:
  sum=0
  for i in range(1,num):
     if num%i==0:
         sum=sum+i
     if sum==num:
      print(num)
     break








