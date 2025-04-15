# 6-2-25 

str1='python is difficult'
#print(str1.replace('difficult','easy')) #direct method (inbulit)

listofstring=str1.split()  #['python', 'is' ,'difficult']


for i in range(len(listofstring)):
    if listofstring[i]=='difficult':
        listofstring[i]='easy'

str2=' '.join(listofstring)
print(str2)

print(f'original str is --{str1}')
print(f'modified str is --{str2}')

'--------------------------------------------------------'

list1=[1,2,4,5]

sum1=0

for i in range(1,6):
    sum1= sum1 + i

sum2=sum(list1)

MissingNumber=sum1-sum2

print(f'missing number is {MissingNumber}')

'-------------------------------------------------------'



#  2  4   8    14    22    32 print it

s=2
for i in range(1,8):
    print(s,end=' ') 
    s+=i*2
    
