'''
dict
-------
var= {k1:v1,k2:v2,....}

student= {'name':'jay','city':'pune','mobileNo':5544255545}

key:
------
immutable and unique

int
float
complex
str
bool
tuple
frozenset

'''

result={1:89,2:78,1:78}
print(result)

result={'mayur':98,'ajay':78}
print(result)

chapter={1.1:'oop',1.2:'class and project'}
print(chapter)

'''values
both=> mutable and immutable
duplicates allowed

'''
'''
1. create a dict to represent single student data
name  city  percentage  marks
'''

A={'name':'Adarsh','city':'ichalkaranji','per':68,'marks':{'python':68,'aws':68}}
print(A)

PythonBatch1225={
    1:{'name':'Adarsh','city':'ichalkaranji','per':68,'marks':{'python':68,'aws':68}},
      2: {'name':'pruthvi','city':'warna','per':68,'marks':{'python':68,'aws':68}},
        3:{'name':'pratik','city':'kolhapur','per':68,'marks':{'python':68,'aws':68}}
}
print(PythonBatch1225)

MobileInfo={'Brand':'XIOMI','model':'Note 9 Pro','RAM':'6+2GB','ROM':'128GB','Colour': 'blue','Processor': 'SnapDragon'}
print(MobileInfo)

Mobiles={ 
    'mNote 9 Pro':{'Brand':'XIOMI','RAM':'6+2GB','ROM':'128GB','Colour': 'blue','Processor': 'SnapDragon'},
    'Redmi9':{'Brand':'XIOMI','RAM':'4','ROM':'64GB','Colour': 'blue','Processor': 'OctaCore'},
    'Redmi 8 pro':{'Brand':'XIOMI','RAM':'8','ROM':'256GB','Colour': 'Black','Processor': 'Dimencity'}}
print(Mobiles)


 

emp ={'name':'ABC','id':101,'dept':'Developer','salary':50000}

TCS = {'HR':{'101':{'name':'ABC','salary':50000,'city':'Kolhapur'},
             '102':{'name':'DEF','salary':55000,'city':'Pune'},
             '103':{'name':'GHI','salary':60000,'city':'Solapur'}
             },
       'Developer': {'204':{'name':'JKL','salary':70000,'city':'Mumbai'},
                     '205':{'name':'MNO','salary':58000,'city':'Pune'},
                     '206':{'name':'PQR','salary':60000,'city':'Kolhapur'}
                     }}
print(TCS)

Kiran_Academy = {
    'java_Batch':{1205:{'101':{'name':'ABC','city':'Kolhapur','per':80},
                        '102':{'name':'DEF','city':'Pune','per':80},
                        '103':{'name':'GHI','city':'Solapur','per':80}}
                        ,
                  1206:{'201':{'name':'JKL','city':'Mumbai','per':80},
                        '202':{'name':'MNO','city':'Pune','per':80},
                        '203':{'name':'PQR','city':'Kolhapur','per':80}}
                     },
    'Python_Batch':{1220:{'301':{'name':'JKL','city':'Mumbai','per':80},
                          '302':{'name':'MNO','city':'Pune','per':80},
                          '303':{'name':'PQR','city':'Kolhapur','per':80}}
                     ,
                    1225:{'401':{'name':'JKL','city':'Mumbai','per':80},
                          '402':{'name':'MNO','city':'Pune','per':80},
                          '403':{'name':'PQR','city':'Kolhapur','per':80}}
                     }
}
print(Kiran_Academy)

'''How to add data into Dict
syntax 
var[key]=value
'''

details={'name':'raj','salary':89000}
print(details['salary'])  #values can be accesed with key

emp ={101:{'name':'ABC','id':101,'dept':'Developer','city':'ichalkaranji','salary':50000},102:{'name':'CDE','id':102,'dept':'Developer','salary':60000}}
print(emp[101])
print(emp[102]['salary'])
print(emp[101]['city'])


emp[102]['city']='kolhapur'
print(emp[102])



fav_actor = {
    'Hrithik Roshan':{
        'War': {
    'Director': 'Siddharth Anand',
    'Producer': ['Aditya Chopra'],
    'Lead_actor': 'Hrithik Roshan, Tiger Shroff',
    'Budget': '150 cr',
    'Collection': '475.5 cr'
},
'Fighter': {
    'Director': 'Siddharth Anand',
    'Producer': ['Viacom18 Studios', 'Marflix Pictures'],
    'Lead_actor': 'Hrithik Roshan, Deepika Padukone',
    'Budget': '250 cr',
    'Collection': 'TBD'  
},
'Super 30': {
    'Director': 'Vikas Bahl',
    'Producer': ['Sajid Nadiadwala', 'Phantom Films', 'Reliance Entertainment'],
    'Lead_actor': 'Hrithik Roshan',
    'Budget': '60 cr',
    'Collection': '208.93 cr'
}

}
}
print(fav_actor)
fav_actor['Hrithik Roshan']['Super 30']['Director']='pratik jadhav'
print(fav_actor['Hrithik Roshan']['Super 30']['Director'])



'''fav_hero = { 'Akshay Kumar':
                    {'Movies':
                            {1: {'movie':'Sooryavanshi', 
                            'Verdict': 'super Hit', 
                            'Budget': '160cr', 
                            'rel_date': '4 November 2021',  
                            'Worldwide Gross': '294cr'}},

                            {2: {'movie': 'Airlift','Verdict': 'Super Hit', 
                            'Budget': '60cr', 
                            'rel_date': '22 January 2016',  
                            'Worldwide Gross': '227cr'}},

                            {3:{'movie':'Rustom', 
                            'Verdict': 'Super Hit', 
                            'Budget': '65cr', 
                            'rel_date': '12 August 2016',  
                            'Worldwide Gross': '218cr'}}
                            }}

print(fav_hero)'''

states={'karnataka':'bengluru','maharashtra':'bombay'}
print(states)

india={'karnataka':{
          'belgavi':{'nippani','chikodi','haveri'},
          'mysure':{'Nanjangud','Sargur','Mysuru'}
          },
        'maharashtra':{
          'kolhapur':{'kagal','panhala','shirol'},
          'sangali':{'miraj','jath','vita'}
          }
       }
print(india)

# HOW TO DELETE DATA FROM DICTIONARY

#1 del keyword
# syntaxx--
#     del var [key] 

square={1:1,2:4,3:9,4:16}
del square[3]
print(square)  #{1: 1, 2: 4, 4: 16}

#pop()---
# syntax--- 
#        var.pop(key)  =>value

square={1:1,2:4,3:9,4:16}
print(square.pop(4))

#HOW TO UPDATE DATA IN DICT

#1 var[key]= value

details={'name':'kunal','city':'pune'}
details['city']='mumbai' #replaces or updates

details['age']=21  #adds new key and value

print(details)

#keys()---- Returs all keys

details={'name':'kunal','city':'pune'}
print(details.keys())

Kiran_Academy = {
    'java_Batch':{1205:{'101':{'name':'ABC','city':'Kolhapur','per':80},
                        '102':{'name':'DEF','city':'Pune','per':80},
                        '103':{'name':'GHI','city':'Solapur','per':80}}
                        ,
                  1206:{'201':{'name':'JKL','city':'Mumbai','per':80},
                        '202':{'name':'MNO','city':'Pune','per':80},
                        '203':{'name':'PQR','city':'Kolhapur','per':80}}
                     },
    'Python_Batch':{1220:{'301':{'name':'JKL','city':'Mumbai','per':80},
                          '302':{'name':'MNO','city':'Pune','per':80},
                          '303':{'name':'PQR','city':'Kolhapur','per':80}}
                     ,
                    1225:{'401':{'name':'JKL','city':'Mumbai','per':80},
                          '402':{'name':'MNO','city':'Pune','per':80},
                          '403':{'name':'PQR','city':'Kolhapur','per':80}}
                     }
}
print(Kiran_Academy.keys())  #dict_keys(['java_Batch', 'Python_Batch'])
print(Kiran_Academy['java_Batch'].keys())  #dict_keys([1205, 1206])

d={'name':'kunal','city':'pune','age':21}
obj=d.values()
print(type(obj))    #<class 'dict_values'>

print(d.items())   #dict_items([('name', 'kunal'), ('city', 'pune')])

print(d.get('age'))  #21

print(d.pop('age'))  #=>>21

# pop
# popitems
# setDefault

#ITERATION

d={'name':'rahul','age':21}
for i in d:
    print(i)   #when we apply for loop on dictionary key will iterate


d={'name':'rahul','age':21}
for key in d:
    print(d[key])   #by using key we can iterate values

#values method

for i in d.values():
    print(i)
    print(i)        #to get value use .values method

for i in d.items():
    print(i)        #to iterate both keys and values

for i,j in d.items():
    print(i,j)        #unpacking the tuple to get both key and values diffrently

#create a dictionary to represent square of numbers 1-20

square={}
for i in range(1,21,1):
    square[i]=(i*i)
print (square)

# increse salary by 2000 
emp={'aditya':5000,'pratik':6000,'raj':7000}
for i in emp:
    emp[i] += 2000
print(emp)

for name,sal in emp.items():
    emp[name]=sal+2000
print(emp)


for name,sal in emp.items():
    emp[name]= sal + sal*(8/100)
print(emp)



# how to delete data
# how to update data
# how to update data
# how to iterate values from dict

hremp={101:{'name':'rajesh','salary':70000},101:{'name':'rahul','salary':50000}}

# for i in hremp:
#     for j in 101:
#         name.__reversed__()

# print(hremp)

for a,b in emp.items():
    for c,d in b:
        print(name) 

