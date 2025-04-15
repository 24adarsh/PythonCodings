


DB = {1:{'item':'poha','rate':20},2:{'item':'tea','rate':10},3:{'item':'idli','rate':10},4:{'item':'VdaPaav','rate':10},3:{'item':'Appe','rate':10}}

print('-'*130)
print('Nasta Center'.center(130))
print('-'*130)

print('''MENU
    1.poha       20rs
    2.tea        10rs
    3.idli       10rs
    4.vdapaav    10rs
    5.appe       20rs
      ''')
choice = int(input("Enter Number : "))
if choice==1:
    quantity=int(input('quantity:'))
    DB[choice]['quantity'] = quantity
    TotalPrize=DB[choice]['quantity']*DB[choice]['rate']
    DB[choice]['TotalPrize'] = TotalPrize
    print(TotalPrize)
elif choice==2:
    quantity=int(input('quantity:'))
    DB[choice]['quantity'] = quantity
    TotalPrize=DB[choice]['quantity']*DB[choice]['rate']
    DB[choice]['TotalPrize'] = TotalPrize
elif choice==3:
    quantity=int(input('quantity:'))
    DB[choice]['quantity'] = quantity
    TotalPrize=DB[choice]['quantity']*DB[choice]['rate']
    DB[choice]['TotalPrize'] = TotalPrize
elif choice==4:
    quantity=int(input('quantity:'))
    DB[choice]['quantity'] = quantity
    TotalPrize=DB[choice]['quantity']*DB[choice]['rate']
    DB[choice]['TotalPrize'] = TotalPrize
elif choice==5:
    quantity=int(input('quantity:'))
    DB[choice]['quantity'] = quantity
    TotalPrize=DB[choice]['quantity']*DB[choice]['rate']
    DB[choice]['TotalPrize'] = TotalPrize
else:
    print('choice is invalid')

print('-'*130)
print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^30}|'.format('choice','item','quantity','rate','TotalPrize'))
print('-'*130)
sum=0
for choice in DB:
    print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^30}|'.format(choice,DB[choice],DB[choice]['item'],DB[choice]['quantity'],DB[choice]['TotalPrize']))
print('-'*130)


print('thank you')
print('visit again.... ')