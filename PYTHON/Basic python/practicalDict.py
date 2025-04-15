details={'anup':273637272,'chaitali':876256372727}

#1
print(details)

#2
details['student3'] = 57584974938
print(details)

#3
details['anup'] = 9876543210
print(details)

#4
del details['anup']
print(details)

#5
print(details['student3'])

#6
print(details.values())

#7
print(details.keys())

#8
user_input = input("Enter an Mobile number: ")
a = int(user_input)
print(f"The integer you entered is: {a}")
for i,j in details.items():
    if j==a:
        print(f'{i}')
        break
else:
    print('mobile number not found')


# Checking if the number is a power of 2

number = int(input("Enter a number: "))

if number > 0:
    while number % 2 == 0:
        number = number // 2
    if number == 1:
        print("The number is a power of 2.")
    else:
        print("The number is not a power of 2.")
else:
    print("The number is not a power of 2.")







