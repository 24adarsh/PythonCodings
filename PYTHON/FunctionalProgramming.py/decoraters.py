# def deco(fun):
#     def inner():
#         fun()
#         print('hello')
#         print('hello')
#     return inner

# @deco
# def printr():
#     print('hello')
#     print('world')
# printr()

# ==========================================

# def deco(fun):
#     def inner(n1,n2,n3):
#         result=fun(n1,n2)
#         # return result+n3 
#         return result-n3 
#     return inner

# @deco
# # def sum(n1,n2):
# #     return n1+n2
    
# # print(sum(10,20,30))

# def sub(n1,n2):
#     return n2-n1

# print(sub(10,20,30))

def login(fun):
    def inner():
        user={'email':'adarsh@gmail.com','password':'123456'}
        email=input('enter ur email : ')
        password=input('enter ur password: ')
        if email==user['email'] and password==user['password']:
            fun()
        else:
            return 'invalid crediantials'
    return inner

@login
def dashboard():
    print('WELCOME TO DASHBOARD')
print(dashboard())

