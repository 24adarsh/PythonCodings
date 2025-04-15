'''map function 

if a operation is done on each element of iterable then this function is used'''

l=[10,20,30,40,50]
print(list(map(lambda num : num+2 ,l)))

student = ['raj','aditya','vaishhnavi','gayatri','amit']
print(list(map(lambda name : len(name) ,student)))     #print list of length of elements

print(list(map(lambda name : name.capitalize() ,student)))  #captilize first letter


'''reduce function

from functools import reduce
reduce(function,iterable)'''

from functools import reduce
l=[10,20,30,40,50]
print(reduce(lambda x,y:x+y,l))   #ADDITION OF ELEMENTS



# result={'math':76,'phy':58,'chem':89}
# increse marks by 2  
# print(dict(map(lambda item:  item[1] + 2,result.values())))

result = {'math': 76, 'phy': 58, 'chem': 89} #increase marks by 2
print(dict(map(lambda i: (i[0], i[1] + 2), result.items())))   #map
print(dict(filter(lambda t:t[1]>72,result.items)))             #filter



emp={'varun': 76000, 'raj': 58000, 'pavan': 89000}
print(dict(map(lambda i: (i[0], i[1] + i[1]*0.1 ), emp.items())))