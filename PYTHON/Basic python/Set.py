print('FROZENSET')
'''
frozenset => 
frozenset({11,22,33})
#Immutable
#heterogeneous set of immutable elements
#duplicates are not allowed
'''
f=frozenset({11,22,33})
print (f)
print(type(f))


print('----------------------------')

print("SET")

s={11,22,33,44}
s.add(999)
print(s)

# heterogeneous collection of immutable elements
s={11,22.45,'raj',True}
print(s)

# methods of set 
'''
add()
syntax
   var.add(value)
'''
s={11,22,33,44}
s.add(55)
print(s)

'''Delete data from set
1.remove
2.discard
3.pop()
4.clear
5.del'''

'''remove:delete data /element
Remove an element from a set; it must be a member.
If the element is not a member, raise a KeyError.
          var.remove(value)
'''
s.remove(33)
print(s)

'''discard : Remove an element from a set if it is a member.
Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.
       var.discard(value)'''

s.discard(22)
print(s)

'''pop
 '''

s.pop()
print(s.pop())
print(s)

'''clear
'''

s.clear()
print(s)

'''del'''

l=[11,22,33,44]

from sys import getsizeof


