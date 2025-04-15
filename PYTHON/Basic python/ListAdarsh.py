
# all fundamental datatypes are immutable: non changeble

name='the keeran academy'
nm=name.replace('ee','i')
print(nm)
print(id(name))
print(id(nm))


# list are mutable 
# it is ordered,mutable,heterogeneous collection of elements where duplicates are allowed

roll=1
passed=[1,5,6,7,8,9,14]

name='rajesh'
students=['kunal','vijay','rahul']
print(id(students))
print(type(students))

cities=['ichalkaranji','kolhapur','jaysingpur','miraj','sangali']
print(type(cities))

students.append('arun')
print(students)

# list is heterogeneous collection of elements
x=[11,12,22,10+7j,True]
print(x)

# in list duplicates are allowed
y=[11,22,33,55,11,44,22]
print(y)


#how to access data from list

x=[11,22,33,['vijay','ajay','sujay'],44,55,66]
print(x)
print(x[2])
print(x[-3])
print(x[3][1])

x=[11,22,33,['vijay','ajay',[77,88,99],'sujay'],44,55,66]
print(x[3][2][1])
# print(x[-3][-1][-1])

print(x[0]+x[3][2][1])
print(x[-4][-3].upper())
print(x[3][0][0:-2:1])    #slicing
print(x[3][3][::-1]) #slicing

l=[11,22,33,44]
print(l[1:3:1])
print()



l=[11,22,33,44,['vijay','ajay','sujay',[1,2,3,4]]]
print(l[4][1:-5:-1])
print(l[4][3][1:4:1])


#methods of list 
# how to add data into list using append and insert

#append---

l=[11,22,33,44]
l.append(55)
print(l)

student=['raj']
student.append('jay')
print(student)

#insert---

l=[11,22,33,44]
l.insert(2,55)
print(l)

student=['raj','jay']
student.insert(1,'sujay')
print(student)

l=[11,22,33,44,['raj','pavan',[1,2,5,6,7],'ajay','vijay'],66,77,88]

l.insert(5,55)
print(l)

l[4].append('sujay')
print(l)

l.insert(8,777)
print(l)

l[4][2].insert(2,3)
l[4][2].insert(5,66)
print(l)

# how to delete data from list

# 1 remove()
# 2 pop()
# 3 clear()
# 4 del


# if REMOVE used it delete only first occurence 
# POP deletes with index values

l=[11,22,33,333,44,22,55,66]
print(l.remove(333))
n=l.pop(4)
print(l)

l=[11,22,33,['raj','pavan','kunal','raj','ajay',[1,2,3,4,2,5],'jayesh'],44,33,55]
n=l.pop(-2)
print(l)

n=l[3].pop()
print(l)

n=l[3].pop(1)
print(l)

n=l.pop()

l[3][4].append(n)
print(l)

# CLEAR deletes all elements

m=[11,22,33,44]
m.clear()
print(m)

# DEL deletes particuler indexed value

l=[11,22,33,[1,2,3],44]
del l[0]
del l[-2][1]
print(l)
del l

# update data using indexing and slicing

l=[11,22,333,44,55]
l[2]=33
print(l)

l=[11,22,33,444,555,666,77]
l[3:-1]=[44,55,66]
print(l)

l=[11,12,13,14,15,16]
del l[1:3]
print(l)


'''
count ---returns number of occurrences of value.
  syntax---
      (method) def count(
      value: int,
      /
      ) -> int
'''
'''
index
Return first index of value.
Raises ValueError if the value is not present.
   syntax--
     (method) def index(
    value: int,
    start: SupportsIndex = 0,
    stop: SupportsIndex = sys.maxsize,
    /
) -> int

'''
'''
reverse-- reverses the list
  syntax--

 (method) def reverse() -> None
'''
l=[11,12,13,14,15,16]
l.reverse()
print(l)

 
 

'''
sort
Sort the list in ascending order and return None.
The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).
If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.
The reverse flag can be set to sort in descending order.
  syntax--
  (method) def sort(
    *,
    key: None = None,
    reverse: bool = False
    ) -> None
'''

l=[3,6,1,5,2]
l.sort()
print(l)

l.sort(reverse=True)
print(l)

student=['raj','dev','pruthvi','prstik']
student.sort()
print(student)

'''differnce between sort and sorted 
sort is method |changes in original
sorted is funtction |not changes original
'''
'''
diff between append and extend 
appends add a single element at the end of list
extend adds a multiple elements at the end of a list

'''
# interview questions
# how to access data from list 
# how to delete data from list 
# how to update data of list 
# what is difference between <<<<<

my_list = [0] * 5
print(my_list)
print(sum(my_list))

my_list = ['a', 'b', 'c']; 
my_list[1:2] = ['d', 'e']

