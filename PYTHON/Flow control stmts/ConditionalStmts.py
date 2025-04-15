# IF Statement 
    # syntax--- 

# if cond:
#     stmt1
#     stmt2


# age=eval(input('enter age: '))
# if age >=18:
#     print(f'u are eligible for voting')
# print('thank u')

# n1 = eval(input('enter n1:'))  #  number
# n2 = eval(input('enter n2:'))  #  divisor1
# n3 = eval(input('enter n3:'))  #  divisor2
# if  n1 % n2 == 0 & n1 % n3 == 0:
#     print(f"number is divisible by {n2} , {n3}")

# numbers=[11,22,33,44,55,66,77]
# for i in numbers:
#     i%2==0
#     print(i)

# for i in numbers:
#     if i>40:
#         print(i)

# for i in numbers:
#     if i>30 and i<60:
#         print(i)

# numbers=[11,22,33,44,55,66,77] 

# #even
# for num in numbers:
#     if num%2==0:
#         print(num)
# #odd
# for num in numbers:
#     if num%2!=0:
#         print(num)

result={'saurabh':89,'kunal':32,'rahul':49,'harish':23}
#Print list of name of student =>PASSED

passed=[]
for i,j in result.items():
    if j>35:
     passed.append(i)
    print(passed)


emp={'saurabh': 89000, 'kunal': 72000, 'rahul':49000,'harish': 23000}

for name, sal in emp.items():
   if sal<50000:
      emp[name]=sal+sal*10/100
print(emp)


# 17/1/2025
'''
Flow Control Statements:

1. Conditional Statements :
2. Iterative statements
3. Transfer statements

'''

'''
1. Conditional Statements :
    1. if statements :
        syntax :
            if condition:
                body of code         # minimum 1 space is required up to 4 space for indentation
                statements
            # if condition is true or satisfi then it enter in the body of if 

    2. if else statements :
        syntax :
            if condition:
                statement 1
                statement 2 
            else:
                statement 3



    3. if elif else statements :
        syntax:
            if condition 1:
                statement1
                statement2
                
            elif condition 2:
                statement3
                statement4
                
            elif condition 3:
                statement5
                statement6
                 
            else:
                statement7


'''

# age = eval(input('Enter age : '))
# if age >= 18:
#     print('You are eligible for voting')
# print('Thank you')

# n = eval(input("enter a no. : "))
# if n%2==0:
#     print(f"{n} is divisible by 2")

# n = eval(input("enter a no. : "))
# if n%3==0 and n%4==0:
#     print(f"{n} is divisible by 3 and 4")

'''
WAP to iterate only number which is greater than 40
WAP to iterate only number which is between 30 and 60

'''
# numbers = [11,22,33,44,55,66,77]
# for i in numbers:
#     if i >=40:
#         print(i,end=',')
# print()
# for i in numbers:
#     if 30 <= i <=60:
#         print(i,end=',')
'''
WAP to print negative numbers from list
'''
# num = [-11,22,-33,44,55,-66,77]
# for i in num:
#     if i<0:
#         print(i)

'''
WAP to iterate even no.s from list
'''
# num = [11,22,33,44,55,66]
# print("Even numbers from list : ",end='')
# for i in num :
#     if i%2==0:
#         print(i,end=',')

'''
WAP to iterate odd no.s from list
'''
# print("\nodd numbers from list : ",end='')
# for i in num :
#     if i%2!=0:
#         print(i,end=',')

'''
print list of name students which are passed 
'''
# result = {'sourabh':89,'kunal':32,'rahul':49,'harish':23}
# passed = []
# for i in result:
#     if result[i] >=40:
#         passed.append(i)
# print('Passed students :',passed)

'''
increase salary by 10% whose salary is less than 50000
'''
# emp = {'sourabh':89000,'kunal':32000,'rahul':49000,'harish':23000}
# for i in emp:
#     if emp[i]<50000:
#         emp[i] += emp[i] * 0.10
# print('Updated salary : ',emp)


'''
Interview Questions : 
What is flow control statement ?
what are types of flow control statement ?
What is purpose of conditional statement ?
What are types of conditional statement ?
Explain if statement with example ?

'''
# 20/1/2025
'''
2. if else statements :
        syntax :
            if condition:
                statement 1
                statement 2 
            else:
                statement 3

'''
# per = 85
# if per>90:
#     print('You are eligible for government colllege.')
# else:
#     print('You are eligible for private colllege.')
# print('Thank You.')

'''
eligible for vote
'''
# age = int(input('Enter your age : '))
# if age>=18:
#     print("Yes, you are eligible for voting.")
# else:
#     print("No, you are not eligible for voting.")


'''
WAP to check a number is even or odd
'''
# num = int(input("Enter a number : "))
# if num%2==0:
#     print(num,'is even')
# else:
#     print(num,'is odd')

'''
print list of even no.s and odd no.s
'''
# numbers = [1,2,3,4,5,6,7,8,9,10]
# odd=[]
# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Odd numbers : ",odd)
# print("Even numbers : ",even)

'''
wap to print list of names of passed and failed student
'''
# result = {'rajesh':78,'amar':32,'vijay':69,'kunal':30}
# passed=[]
# failed=[]
# for i,j in result.items():
#     if j >=40:
#         passed.append(i)
#     else:
#         failed.append(i)
# print(passed)
# print(failed)

'''
3. if elif else statements :
        syntax:
            if condition 1:
                statement1
                statement2
                
            elif condition 2:
                statement3
                statement4
                
            elif condition 3:
                statement5
                statement6
                 
            else:
                statement7
'''
# num = eval(input("Enter a number : "))
# if num>0:
#     print("Positive number")
# elif num<0:
#     print("Negative number")
# else:
#     print("number is zero")

'''

'''
# ram = int(input("Enter your age : "))
# sham = int(input("Enter your age : "))
# raj = int(input("Enter your age : "))

# if ram > sham :
#     if ram >raj:
#         print("Ram is big ")
# elif sham >raj:
#     print("Sham is big")
# else:
#     print("Raj is big")

# if ram > sham and ram>raj:
#     print("Ram is big ")
# elif sham >raj and sham> ram:
#     print("Sham is big")
# else:
#     print("Raj is big")

'''
Interview Questions : 
    1. What is purpose of else?
    2. What is purpose of elif?
    3. What is difference between 
        1.if elif statements and multiple if statements

'''

'''
what is flow control statements in python and types?
->conditional,looping , transfer

'''