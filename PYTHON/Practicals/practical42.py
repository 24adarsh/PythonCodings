terms=int(input('enter how many terms u want to print : '))
n1=0
n2=1
l=[]
for i in range(terms):
    # print(n1,end=' ')
    l.append(n1)
    n1,n2=n2,n1+n2
    # n1=n2
    # n2=n1+n2
# l.reverse()
print(l[::-1])