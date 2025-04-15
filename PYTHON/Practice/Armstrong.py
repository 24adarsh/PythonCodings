num=int(input('enter a number : '))
num1=str(num)
sum=0
digit=len(num1)

for i in num1:
    sum = sum + int(i)**digit

if sum == num:
    print('its Armstrong number')
else:
    print('its not Armstrong number')



# num = int(input('enter a number : '))
# num1 = str(num)
# sum = 0
# digit = len(num1)

# for i in num1:
#     sum = sum + int(i) ** digit 

# if sum == num:  
#     print('its Armstrong number')
# else:
#     print('its not Armstrong number')

