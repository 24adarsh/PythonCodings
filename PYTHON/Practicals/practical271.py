import copy
# random.py file 
# def shuffle(sequence): 
#   pass 

# from random import shuffle
# x=[30,10,20]
# shuffle(x)
# print(x)

# for primitive elements like int, string copy and deepcopy output is same for non primitive objects like 

# list=[1,[2,10],3,4]
# newlist=copy.copy(list) #shallow clonning it means changes done on duplicate shows on original also

# print(list is newlist)
# print(list==newlist)

# newlist=copy.deepcopy(list)

#deepcopy and copy both will provide deep clonning if elements are primitive types
# means if we change duplicates original will be unaffected
#but if members of list were objects then shollow clonning will be given by copy()here
#change in duplicates will be reflected in original alos
#deepcopy() will give deep clone where duplicate change is not reflected in original

list1=[1,2,3]
list2=[1,2,3]

print(list1==list2)
print(list1 is list2)

