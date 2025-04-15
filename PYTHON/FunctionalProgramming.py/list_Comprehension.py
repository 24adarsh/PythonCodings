#8-2-25
# nl=[exp for var in iterable if condition] .

l=[1,2,3,4,5]   #simple method
square=[]
for num in l:
    sq=num**2
    square.append(sq)
print(square)

nl=[ num**2 for num in l]   #list comprehension
print(nl)

# print square of even numbers only.

l=[1,2,3,4,5]
square=[]
for num in l:
    if num%2==0:
        square.append(num**2)
print(square)

square=[num**2 for num in l if num%2==0]
print(square)


# nl=[exp1 if condition else exp2 for var in iterable]

l=[1,2,3,4,5,6]
# if num is sum make square if num is odd make cube 

nl=[num**2 if num%2==0 else num**3 for num in l]
print(nl)

result={'akshay':34,'adesh':87,'vaishnavi':39,'anushka':91}

# passed=[name for name in result.items() if name > 35]
# print(passed)

# passedFailed=[name.upper()  if name > 35 else name.lower() < 35 for i in result.items()]
# print(passedFailed)

l=[1,2,3,4]

square={num:num**2 for num in l}
print(square)

square={num:num**2 for num in l if num%2==0}
print(square)

sc={num:num**2 if num%2==0 else num**3 for num in l }
print(sc)


result={'akshay':34,'adesh':87,'vaishnavi':39,'anushka':91}

passes = {key: value for key, value in result.items() if value > 35}
print(passes)  

passes = {key: value+2 if value > 35 else value+5 for key, value in result.items() }
print(passes)

numbers = [3,5,45,97,32,22,10,19,39,43]
l=[n for n in numbers if n %2==0]
print(l)


#  Generate a list of characters from a string
# Sample Output
# ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

str1='hello World'
nl=[str2 for str2 in str1 ]
print(nl)

#or

chars = [char for char in str1 if char.isalpha()]
print(chars)

#  Create a list of lengths of words in a sentence
# Sample Output
# This is a sample sentence.
# [4, 2, 1, 6, 9]

strr='This is a sample sentence'
nl2=[len(word) for word in strr.split()]
print(nl2)

# Generate a list of tuples containing a number and its square
# Sample Output
# [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

nl3=[(num,num**2) for num in range(1,6) ]
print(nl3)

# Create a list of lowercase letters
# Sample Output
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nl4=[chr(x) for x in range(ord('a'),ord('z')+1)]
print(nl4)

nl5=[chr(x) for x in range(ord('A'),ord('Z')+1)]
print(nl5)

# Create a list of even numbers squared and odd numbers cubed from 1 to 10
# Sample Output
# [1, 4, 27, 16, 125, 36, 343, 64, 729, 100]

nl6=[i**2 if i%2==0 else i**3 for i in range(1,11)]
print(nl6)