# tuple is comma saparated values within parathesis
# it is ordered immutable heterogeneous collectin where duplicates are allowed 


# how to access data from tuple 
# by using indexing and slicing 

# indexing 
 
'''var[si,ei,sv]
si start index
ei end index
sv step value'''

t=(11,22,33,44,55)
print(t[1])

t=(11,22,[111,222],33,44,(11,22,33),55)
print(t[2][0])
print(t[-2][1])

# slicing

# default values 
# start value 

students=('raj','sham','ram','ajay','vijay','sahil')
print (students[0:-3:1])  
#(raj,sham,ram)
print (students[:-3:1])
#(raj,sham,ram)

students=('raj','sham','ram','ajay','vijay','sahil')
print (students[-1:2:-1])  
#(raj,sham,ram)
print (students[:2:-1])
#(raj,sham,ram)

# end value 

students=('raj','sham','ram','ajay','vijay','sahil')
print (students[3:6:1])    # ('ajay','vijay','sahil')
print (students[3::1])     # ('ajay','vijay','sahil')
print (students[2:-7:-1])  # ('ram', 'sham', 'raj')
print (students[2::-1])    # ('ram', 'sham', 'raj')

# Step value 

students=('raj','sham','ram','ajay','vijay','sahil')
print (students[3:6:1])                  #('ajay', 'vijay', 'sahil')

students=('raj','sham','ram','ajay','vijay','sahil')
print (students[3:6:])                   #('ajay', 'vijay', 'sahil')


name="rameshwaram"
print(name[:3])   #ram
print(name[-3:])  #ram
print(name[:-4:-1])  #mar
print(name[2::-1])  #mar

#what is differnce between list and tuple
  
#   LIST 
''' 1.comma saprated value within []
    2.mutable
    3.[] is  mandatory 
    4.list requres more memory compare to tuple
    5.list is slower to compile compared to tuple 
    6.it manages memory wisely memory sufficient
    7.list supports only unpacking doesnt supports packing
    8.if data is changable then list is used'''

#   TUPLE
''' 1.comma saprated value within ()
    2.immutable
    3.() is not mandatory
    4.tuple requres less memory compare to list 
    5.tuple is faster to compile compared to list
    6.memory insufficient
    7.tuple supports packing and unpacking
    8.if data is Unchangable then Tuple is used'''




from sys import getsizeof

t=(10,20,30,40,50)

l=[10,20,30,40,50]

print(getsizeof(1))
print(getsizeof(t))


#interview questions 
# what is tuple
# what is diff between tuple and list 
# how to check memory size of an object





