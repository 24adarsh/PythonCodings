n=int (input('enter how many numbers u want in series: '))
first=0
second=1
for i in range(n):
    print(first,end= ' ')
    temp=first
    first=second
    second= temp+first