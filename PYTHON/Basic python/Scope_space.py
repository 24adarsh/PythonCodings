'''Space_scope
1.global space
2.local space
'''


# x=100     #global
# def f1():
#     a=10   #local
#     print(a)

# f1()

# x=100     #global
# def f1():
#     a=10   #local
#     print(x)   #we can use global value inside functions

# f1()

# x=100
# y=200     #global
# def f1():
#     a=10 
#     y=300  #local      
#     print(x)           #if value is not present inside function it uses outside value
#     print(y)           #calling function uses inside value

# f1()



# x=200
# y=200
# def f1():
#     y=300
#     global x
#     x=x+100  #to modify global variables value have declare as global first
# f1()


# x=100
# y=200     #global
# def f1():
#     a=10 
#     y=300  #local      
#     return a   #returns throws value to function caller
# a=f1()           

# f1()
# print(a)
# print(f1())


# x=100
# y=200     #global
# def f1():
#     a=10 
#     y=300  #local 
#     b=50     
#     return a,b       #we can use multiple return values    

# f1()
# print(f1())

# def f2():
#     a=10
#     b=20
#     print('welcome')
#     return a
#     print('-----')   #return turminates function 

# f2()
# print(f2())
# print('hello')

'''----------------------------------------------------------------'''

# a=100
# b=200
# def a1():
#     c=300
#     d=400
#     e=a+c
#     print(e)  #global can be used in local functions
# a1()

# a=100
# b=200
# def a1():
#     c=300
#     d=400
# a1()
# # print(c)  we cant use local variable as global 

# a=100
# b=200
# def a1():
#     c=300
#     d=400
#     # a=a+c  we cant update global variable in local space 
#     global a 
#     a=a+c    #we can update global variable with global keyword in local space 
# a1()

# a=100
# b=200
# def a1():
#     c=300
#     d=400
#     return c  #return throws value to function caller
# a1()
# print(a1())

'''=----------------------------------------------------------='''







