'''
COPY MODULE
1. Shellow Copy
2. Deep Copy


'''

#SHELLOW COPY   
'''it created new object for copy but refers to old elements only
it makes new objects for outer shell only inner elements were referd fron original id '''

from copy import copy
l=[[11,22],[33,44]]
nl=copy(l)
print(nl)

print(f'id of l is {id(l)}')     #id of l is 2449031125568
print(f'id of nl is {id(nl)}')   #id of nl is 2449030986496


print(f'id of l[0] is {id(l[0])}')     #id of l[0] is 1346919911808
print(f'id of nl[0] is {id(nl[0])}')   #id of nl[0] is 1346919911808

#outer element
nl[0]='hello'
print(nl)          #['hello', [33, 44]]
print(l)           #[[11, 22], [33, 44]]

#inner element
nl[1][0]='welcome'
print(nl)          #['hello', ['welcome', 44]]
print(l)           #[[11, 22], ['welcome', 44]]

print('----------------------------------------------------------------------------')

#DEEP-COPY
'''it created new object elements '''

from copy import deepcopy
l1=[[11,22],[33,44]]
nl1=deepcopy(l1)
print(nl1)

print(f'id of l1 is {id(l1)}')     #id of l is 2518026528896
print(f'id of nl1 is {id(nl1)}')   #id of nl is 2518026528960


print(f'id of l[0] is {id(l1[0])}')     #id of l[0] is 2518026517440
print(f'id of nl[0] is {id(nl1[0])}')   #id of nl[0] is 2518026529024

#outer element
nl1[0]='hello'
print(nl1)          #['hello', [33, 44]]
print(l1)           #[[11, 22], [33, 44]]

#inner element
nl1[1][0]='welcome'
print(nl1)          #['hello', ['welcome', 44]]
print(l1)           #[[11, 22], [33, 44]]

print('----------------------------------------------------------------------------')

