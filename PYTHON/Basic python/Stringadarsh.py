

name ='Adarsh'
print(name.upper())  #ADARSH
print(name.lower())  #adarsh


name='the kiran academy'
print(name.title())    #The Kiran Academy


name='the kiran academy'
print(name.capitalize())   #The kiran academy


name='the kiran academy'
print(name.isalpha()) #false because of space

name='theKiranAcademy'
print(name.isalpha())     #true

T = "Hello"
x = T.istitle()
print(x)

p = "Hello welcome to pune"
x = p.rfind("e")
print(x)

C = "55"
y = C.isdigit()
print(y)

w = "apple, banana, cherry"
z = w.rsplit(", ")
print(z)


# reverse the string 
name ='rajesh'
rev=''
for char in name:
    rev=char+rev 
print(rev)


