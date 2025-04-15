'''WAP to print numbers from 11 to 20
   WAP to print numbers from 20 to 11
   '''

for num in range(11,21,1):
    print (num)
    
for num in range(20,10,-1):
    print (num)

for num in range(22,31,2):
    print (num)  #even numbers 21-30

for num in range(33,41,2):
    print (num)  #odd numbers 32-40

for num in range(50,30,-2):
    print (num)   #even numbers 50-31

for num in range(99,80,-2):
    print (num)    #odd numbers 100-80

'''WAP to print a square of numbers from 11-15
   WAP to print a cube of numbers from 1-5
   WAP to print a list of numbers from 100-200
   WAP to print a set of numbers from 50-1
   WAP to print a list of square of numbers from 1-10
   WAP to print a set of cube of numbers from 5-1
'''
for num in range(11,16,1):
    print (num*num) 

for num in range(1,6,1):
    print (num*num*num)   
  
l=[]
for num in range(100,201,1):
    l.append(num)
print (l)   #print list from 100 to 200

s=set()
for num in range(50,0,-1):
    s.add(num)
print (s)   #print set of 50 to 1

square=[]
for num in range(1,11,1):
    square.append(num*num)
print (square)

cube=set()
for num in range(1,11,1):
    cube.add(num*num*num)
print (cube)


'''
  WAP to print sum of all numbers from 1-10
  WAP to print mul of all numbers from 1-5
  '''
sum=0
for num in range(1,11,1):
    sum= sum + num
print (sum)   


mul=1
for num in range(1,6,1):
    mul= mul * num
print (mul)   

'''by defaults

start 0
stop 
step 1'''

for num in range(1,6):
    print (num)

for num in range(6):
    print (num)  #by default start 0 step 1







