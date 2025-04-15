'''
file handling
---------------------------

Step1=open
step3=operations
step3=close

'''
# f=open('demo1.txt','r')
# for i in f:
#     print(i)
# print(f.closed)
# f.close()
# print(f.closed)
# #f.read()       #I/O operation on closed file


'''
WITH  --- it closes file automatically after completing the execution of block

with open (file,mode) as f:
           #operation

'''

# with open('demo1.txt','r') as f:
#     for i in f:
#         print (i)
#     print(f.closed)
    
# print('coding......')

# print(f.closed)

'''
Reading and writing

Reading
read()
readline()
readlines()

'''
# f=open('demo1.txt','r')
# # print(list(f))     
# # print(list(f))           #it executes only once


# data=f.read(6)
# print(data)

# f=open('demo1.txt','r')
# data1=f.readline(1)
# print(data1)

# f=open('demo1.txt','r')
# data2=f.readlines()
# print(data2)


''' tell---- defines cursors present location
# seek---- sets cursors location manually '''

# f=open('demo1.txt','r')
# print(f.tell())    #finds cursor location
# data=f.read(6)
# print(f.tell())

# f.seek(8)           #sets cursor location
# data1=f.read(6)
# print(data1)

'''
WRITING
---------------
MODES=> 'w' 'a' 'x'
        write append check presence

'''

'''
modes
--------------
r == only read
w == only write
r+ or w+ == readable or 
'''

# f=open('demo1.txt','r')
# print(f.readable())     #True

# f=open('demo1.txt','w')
# print(f.writable())      #True

# f=open('demo1.txt','r+')
# print(f.readable())       #True
# print(f.writable())       #True