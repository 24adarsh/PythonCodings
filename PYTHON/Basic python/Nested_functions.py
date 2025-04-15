# ''''nested function:--
#         functons inside another function
        
#         '''

# def f1():
#     print('outer function')
#     x=100
#     def f2():
#         print('inner function')
#         y=200
#         return y
#     f2()
# f1()

# def f1():
#     print('outer function')
#     x=100
#     def f2():
#         print('inner function')
#         y=200
#         return y
#     return x,f2
# x,f2=f1()
# print(x+y)


# def f1():
#     print('outer function')
#     x=100
#     def f2():
#         print('inner function')
#         y=200
#         return y
#     y=f2()
#     return x,f2()
# x,y=f1()
# print(x+y)

# def m1():
#     name='vaibhav'
#     def m2():
#         age='25'
#         def m3():
#             city='pune'
#             return city
#         city=m3()
#         return age,city
#     age,city=m2()
#     return name,m2()
# name,age,city=m1()
# m1()

# print(f'my name is{name}i am {age}year old im from {city}')
