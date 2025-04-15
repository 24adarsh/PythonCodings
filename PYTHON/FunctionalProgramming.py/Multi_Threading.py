# def print_1_10():
#     for i in range(1,11):
#         print(i)

# def print_21_30():
#     for i in range(21,31):
#         print(i)

# print ('The end')

# from threading import Thread

# t1=Thread(target=print_1_10)
# t2=Thread(target=print_21_30)

# t1.start()
# t2.start()


#----------------------------------------------------------------


def print_1_10():
    for i in range(1,11):
        print(i)

def print_11_20():
    for i in range(11,21):
        print(i)

from threading import Thread

t1=Thread(target=print_1_10)
t2=Thread(target=print_11_20)

t1.start()
t1.join()
t2.start()
t2.join()

print ('The end')

#====================================================================






