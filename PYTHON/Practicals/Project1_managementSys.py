'''
Management system:

registration
   name
   mo no
   course
        submit to database
    
display -- all student admited today

update-- change course
         mob no
         fees details

delete--- admission camcels or takes refunds

filter----
        filter by batch no 
        by course

search----
        



'''
DB = {101:{'name':'Adarsh Pujari','city':'Ichalkaranji','email':'adarsh@gmail.com','course':'Python','Total Fee':50000,'Paid Fee':20000,'Remaining Fee':30000}}

account_id_pass = {}

print('-'*130)
print('The Kiran Academy'.center(130))
print('-'*130)

account = int(input("""
1:for Account already created
2:for new login : """))
if account == 1:  
    user_id = input("Enter user Id : ")
    password = input("Enter password : ")
elif account==2:
    user_id = input("Enter user Id : ")
    password = input("Enter password : ")
    account_id_pass[user_id] = password

while True:
    print('''
    1.Admission
    2.Record
    3.Update
    4.Delete
    5.Filter
    6.Exit
    ''')
    choice = int(input("Enter your choice : "))
    if choice==1:
            reg_no = int(input("Enter registration number : "))
            name = input("Enter name : ")
            city = input('Enter city : ')
            email = input('Enter email : ')

            
            while True:
                if not email.islower():
                    print("Invalid Email: Email should be in lowercase.")
                    email = input('ReEnter email : ')
                    break
                elif not email.endswith('@gmail.com'):
                    print("Invalid Email: Email should end with '@gmail.com'.")
                    email = input('ReEnter email : ')
                    break

                invalid_char_found = False
                for ch in email:
                    if not (ch.isalnum() or ch in {'@', '.'}):  
                        invalid_char_found = True
                        break  
                    
                if invalid_char_found:
                    print("Invalid Email: Contains invalid characters.")
                    email = input('ReEnter email : ')
                    continue
                else:
                    break

            course = input('Enter course : ')
            paid_fee = eval(input("Enter fee : "))

            total_fee = 50000
            
            if course=='Python':
                total_fee = 55000
            elif course=='Java':
                total_fee = 40000

            remaining_fee = total_fee - paid_fee

            DB[reg_no] = {'name':name,'city':city,'email':email,'course':course,'Total Fee':total_fee,'Paid Fee':paid_fee,'Remaining Fee':remaining_fee}
        
    elif choice==2:
        print('-'*130)
        print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format('reg_no','name','city','email','course','Total Fee','Paid Fee','Remaining Fee'))
        print('-'*130)
        for reg in DB:
            print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format(reg,DB[reg]['name'],DB[reg]['city'],DB[reg]['email'],DB[reg]['course'],DB[reg]['Total Fee'],DB[reg]['Paid Fee'],DB[reg]['Remaining Fee']))
            print('-'*130)

    elif choice==3:
        reg_no = int(input("Enter a register number : "))
        if reg_no in DB:
            while True:
                print('''
                    Which information you want to update : 
                    1.Name
                    2.City
                    3.Email
                    4.Course
                    5.Fee
                    6.Exit
                ''')
                choice = int(input("Enter your choice : "))
                if choice==1:
                    Up_name = input("Enter your updated name : ")
                    DB[reg_no]['name'] = Up_name
                    print("Update Successfully............")

                elif choice==2:
                    Up_city = input("Enter your updated city : ")
                    DB[reg_no]['city'] = Up_city
                    print("Update Successfully............")

                elif choice==3:
                    Up_email = input("Enter your updated email : ")
                    DB[reg_no]['email'] = Up_email
                    print("Update Successfully............")

                elif choice==4:
                    Up_course = input("Enter your updated course : ")
                    DB[reg_no]['course'] = Up_course
                    print("Update Successfully............")

                elif choice==5:
                    Up_fee = input("Enter your updated fee : ")
                    DB[reg_no]['fee'] = Up_fee
                    print("Update Successfully............")

                elif choice==6:
                    break
                else:
                    print("Invalid Input")
        else:
            print("Invalid registration numbre.......")
                
            
    elif choice==4:
        reg_no = int(input("Enter your register number which you want to delete the details : "))
        if reg_no in DB:
            del DB[reg_no]
            print("Delete Successfully............")
        else:
            print("Invalid registration numbre.......")

    elif choice==5:
        while True:
            print('''
            choose how to filter : 
            1.Name
            2.City
            3.Email
            4.Course
            5.Fee
            6.Exit
            ''')
            filter = int(input("Enter filter : "))

        
            if filter == 1:
                n = input("Enter name which you want to filter : ")
                print('-'*130)
                print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format('reg_no','name','city','email','course','Total Fee','Paid Fee','Remaining Fee'))
                print('-'*130)
                for reg in DB:
                    if DB[reg]['name']==n:
                        print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format(reg,DB[reg]['name'],DB[reg]['city'],DB[reg]['email'],DB[reg]['course'],DB[reg]['Total Fee'],DB[reg]['Paid Fee'],DB[reg]['Remaining Fee']))
                        print('-'*130)

            elif filter == 2:
                n = input("Enter city name which you want to filter : ")
                print('-'*130)
                print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format('reg_no','name','city','email','course','Total Fee','Paid Fee','Remaining Fee'))
                print('-'*130)
                for reg in DB:
                    if DB[reg]['city']==n:
                        print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format(reg,DB[reg]['name'],DB[reg]['city'],DB[reg]['email'],DB[reg]['course'],DB[reg]['Total Fee'],DB[reg]['Paid Fee'],DB[reg]['Remaining Fee']))
                        print('-'*130)
                

            elif filter == 3:
                n = input("Enter email which you want to filter : ")
                print('-'*130)
                print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format('reg_no','name','city','email','course','Total Fee','Paid Fee','Remaining Fee'))
                print('-'*130)
                for reg in DB:
                    if DB[reg]['email']==n:
                        print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format(reg,DB[reg]['name'],DB[reg]['city'],DB[reg]['email'],DB[reg]['course'],DB[reg]['Total Fee'],DB[reg]['Paid Fee'],DB[reg]['Remaining Fee']))
                        print('-'*130)

            elif filter == 4:
                n = input("Enter course name which you want to filter : ")
                print('-'*130)
                print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format('reg_no','name','city','email','course','Total Fee','Paid Fee','Remaining Fee'))
                print('-'*130)
                for reg in DB:
                    if DB[reg]['course']==n:
                        print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format(reg,DB[reg]['name'],DB[reg]['city'],DB[reg]['email'],DB[reg]['course'],DB[reg]['Total Fee'],DB[reg]['Paid Fee'],DB[reg]['Remaining Fee']))
                        print('-'*130)

            elif filter == 5:
                n = input("Enter fee which you want to filter : ")
                print('-'*130)
                print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format('reg_no','name','city','email','course','Total Fee','Paid Fee','Remaining Fee'))
                print('-'*130)
                for reg in DB:
                    if DB[reg]['fee']==n:
                        print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^8}|{:^10}|{:^10}|{:^15}|'.format(reg,DB[reg]['name'],DB[reg]['city'],DB[reg]['email'],DB[reg]['course'],DB[reg]['Total Fee'],DB[reg]['Paid Fee'],DB[reg]['Remaining Fee']))
                        print('-'*130)
                
            elif filter ==6:
                break
                    
            else:
                print("Invalid Input...............")


    elif choice==6:
        break
    else:
        print("Invalid Input..................")
        