num=int(input('enter number: '))

def checkprime(num):
    for i in range(2,num):
        if num%i==0:
            print(' its not prime number')
        break
    else:
        print(' its  prime number')

print(checkprime(num))
    
