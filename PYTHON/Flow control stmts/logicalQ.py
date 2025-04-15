'''write a program to check number is armstrong or not'''

'''ARMSTRONG NUMBER---
It is a integer that is equal to sum of its digits
---each digit is raised number of digit '''

# num=eval(input('enter number: '))
# num1=str(num)
# digit=len(num1)
# sum=0
# for i in num1:
#     sum=sum+int(i)**digit
# if sum==num:
#     print('yes its armstrong number')
# else:
#     print('NO its not armstrong number')

'''write a program to check number is perfect or not'''

'''PERFECT number----
A perfect number is a positive integer that is equal to the sum of its proper divisors, 
excluding itself'''


# num=eval(input('enter number: '))
# sum=0
# for i in range(1,num):
#     if sum%i==0:
#         sum=sum+i
# if sum==num:
#     print('yes its perfect number')
# else:
#     print('NO its not perfect number')

'''write a program to check str/word is pallindrom or not'''

# word=input('enter word: ')
# rev_w=""    #or rev=word[::-1]
# for i in word:  
#     rev_w=i+rev_w
# print(rev_w)

# if word==rev_w:
#     print(True)
# else:
#     print(False)

'''write a program to calculate factorial of any number'''

# num=eval(input('enter a number: '))
# mul=1
# for i in range(num,0,-1):
#     mul=mul*i
# print (mul)


# intrview questions
# salary=>TDS

'''WAP for fibonacci numbers series'''

# l=[]
# rr=int (input('enter number range : '))
# for i in range(rr):
#     l.append(i)
#     l.append(i[-i])

# print(l)

n1=0
n2=1
for i in range(5):
    print(n1,end=" ")
    n1,n2=n2,n1+n2














