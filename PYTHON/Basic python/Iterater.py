'''18/02/25


ITERATER

list tuple set range dict str ==> ITERABLES

iter()

iterator--- is a objet which helps to iterate the elements of iterables


'''

# l=[11,22,33,44,55]
# #Iterater_object=i
# i=iter(l)
# print(i)
# print(next(i))    #11
# print(next(i))    #22
# print(next(i))
# print(next(i))
# print(next(i))
# #print(next(i))   #StopIterter

# print(type(i))     #<class 'list_iterator'>

# -------------------------------------------------------



'''

Iterator - It contains only __iter__ method

Iterable - It contains both __iter__ and __next__ method

'''

# t=(11,22,33,44,55)
# #Iterater_object=i
# i=iter(t)     
# print(i)
# print(i.__next__())    #11
# print(i.__next__())    #22
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# #print(next(i))

# print(t.__dir__())    #only __iter__ is present so it is iterable
# print(i.__dir__())    #__iter__ and __next__ both are present so it is iterater

#--------------------------------------------------------------------------------------------

'''CREATING OWN RANGE FUNCTION...'''

# class myrange:
#     def __init__(self,start,stop,step=1):
#         self.start=0
#         self.stop=stop
#         self.step=step
#     def __iter__(self):
#         return myrange_iterator(self)
    
# class myrange_iterator:
#     def __init__(self,iterable_obj):
#         self.iterable_obj=iterable_obj
#     def __iter__(self):
#         return self
#     def __next__(self):
#         result=self.iterable_obj.start
#         if self.iterable_obj.start<self.iterable_obj.stop:
#             self.iterable_obj.start=self.iterable_obj.start+self.iterable_obj.step
#             return result
#         else:
#             raise StopIteration
        
# for i in myrange(6):
#     print(i*i)









