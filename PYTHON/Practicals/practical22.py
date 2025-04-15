# terms=10
# result=list(map(lambda x: 2**x,range(terms)))
# print(result)


# for i in range(terms):
#     print('2 raised to power ',i,'is',result[i])


# print('=====================================================')


# # identyfy the pattern relation and WAP for it 
# # 1,3,7,13,21,31

# oldresult=1
# newresult=0
# for i in range(6):
#     newresult=oldresult+(2*i)
#     print(newresult,end=' ')
#     oldresult=newresult


# print('=========================================================')


# # print reversed number

# num=123456
# print(str(num)[::-1])

# print(id(num))
# print(id(str(num)))

# print(str(num))

# str1='hello'
# def count(str1,ch):
#     t=0
#     for i in str1:
#         if ch==i:
#             t=t+1
#     print(ch,'is come ',t,'times')
# #count(str1,'h')
# for ch in set(str1):
#     count(str1,ch)


# import time

# def measure_execution_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
#         return result
#     return wrapper

# # Example usage
# @measure_execution_time
# def calculate_multiply(numbers):
#     tot = 1
#     for x in numbers:
#         tot *= x
#     return tot

# # Call the decorated function
# result = calculate_multiply([1, 2, 3, 4, 5])
# print("Result:", result)




