lower=int(input('enter lower interval: '))
upper=int(input('enter upper interval: '))
for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                print(i,'is not prime')
                break
        else:
            print(i,'is prime')

