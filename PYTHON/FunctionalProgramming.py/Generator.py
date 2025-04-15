def numbers_gen():
    yield 1
    yield 2
    yield 3

gen=numbers_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
#=========================================

def numbers_gen1():
    for i in range(1,101):
        yield i

gen1=numbers_gen1()
print(next(gen1))
print(next(gen1))
#=========================================

def num_gen():
    for i in range(10):
        yield i

gen2=num_gen()
print(next(gen2))
#=========================================

from sys import getsizeof

def read_data_file():
    with open('demo1.txt','r') as file:
        for line in file:
            yield line

gen=read_data_file()
print(gen)
print(getsizeof(gen))

# data=read_data_file.readlines()
# print(data)

n=int(input('enntr no of rows : '))
for row in range(1,n+2):
    for colomn in range(1,row):
        print('*',end=" ")
    print()
