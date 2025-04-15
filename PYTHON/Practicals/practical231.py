'''ANAGRAM'''
# str1=input("enter 1st str : ")
# str2=input("enter 2nd str : ")

# if sorted(str1)==sorted(str2):
#     print('strings are anagram')
# else:
#     print('strings are not anagram')

'''Frequency of string'''

# str='javabykiran'
# for i in str:
#     count=str.count(i)
#     print(f'{i} has appered {count} times')


# str='javabykiran'
# dictionary={}
# for i in str:
#     c=str.count(i)
#     dictionary[i]=c
# print(dictionary)
# for key, value in dictionary.items():
#     print(f'{key} has appered {value} times')

# str='javabykiran'
# dict={}
# def count(str,ch):
#       sum=0
#       for i in range(len(str)):
#          if str[i]==ch:
#             sum=sum+1
#       return sum


# print prime numbers between 1780 to 1840 

# for i in range(1780, 1841):
#     if i < 2: 
#         continue
#     for j in range(2, i): 
#         if i % j == 0:
#             break 
#     else:
#         print(i,'is prime number\n')
      

# for i in range(1780,1841):
#       is_prime=True
#       for j in range(2,i):
#             if i%j==0:
#                   is_prime=False
#                   break
#       if is_prime:
#             print(i,end=" ")


# l=['a','ab','abc']
# t={10,100,1000}

# for i in l:
#     print(i)
# for j in t:
#     print(j)

# d={}
# d.keys()==i
# d.values()==j

# print(d)

d={'name':'rahul','age':21}
for i in d:
    print(i)


for i in range(7,0,-1):
    i-=1
    print('* '*i)

l=[1,2,[3,4],5,6,(7,8)]
#third sum of all elements in list

# Initialize an empty dictionary
my_dict = {}

# Example list to be used as key
key_list = [1, 2, 3]

# Convert list to tuple
key_tuple = tuple(key_list)

# Example tuple to be used as value
value_tuple = (4, 5, 6)

# Add to dictionary
my_dict[key_tuple] = value_tuple

# Print the dictionary
print("Dictionary with list (converted to tuple) as key and tuple as value:")
for key, value in my_dict.items():
    print(f"{key} : {value}")

