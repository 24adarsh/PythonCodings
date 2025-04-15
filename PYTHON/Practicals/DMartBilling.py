
products = {1:{'item':'poha','rate':20},2:{'item':'tea','rate':10},3:{'item':'bulb','rate':10},4:{'item':'earphones','rate':10},3:{'item':'brush','rate':10}}

print('-'*130)
print('Nasta Center'.center(130))
print('-'*130)

print('''MENU
    1.poha       20rs
    2.tea        10rs
    3.bulb       10rs
    4.earphones  10rs
    5.brush      20rs
      ''')
choice = int(input("Enter Number : "))
if choice==1:
    quantity=int(input('quantity:'))
    products[choice]['quantity'] = quantity
    TotalPrize=products[choice]['quantity']*products[choice]['rate']
    products[choice]['TotalPrize'] = TotalPrize
elif choice==2:
    quantity=int(input('quantity:'))
    products[choice]['quantity'] = quantity
    TotalPrize=products[choice]['quantity']*products[choice]['rate']
    products[choice]['TotalPrize'] = TotalPrize
elif choice==3:
    quantity=int(input('quantity:'))
    products[choice]['quantity'] = quantity
    TotalPrize=products[choice]['quantity']*products[choice]['rate']
    products[choice]['TotalPrize'] = TotalPrize
elif choice==4:
    quantity=int(input('quantity:'))
    products[choice]['quantity'] = quantity
    TotalPrize=products[choice]['quantity']*products[choice]['rate']
    products[choice]['TotalPrize'] = TotalPrize
elif choice==5:
    quantity=int(input('quantity:'))
    products[choice]['quantity'] = quantity
    TotalPrize=products[choice]['quantity']*products[choice]['rate']
    products[choice]['TotalPrize'] = TotalPrize
else:
    print('choice is invalid')

print('-'*130)
print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^30}|'.format('choice','item','quantity','rate','TotalPrize'))
print('-'*130)
sum=0
for choice in products:
    print('|{:^7}|{:^30}|{:^10}|{:^30}|{:^30}|'.format(choice,products[choice],products[choice]['item'],products[choice]['quantity'],products[choice]['TotalPrize']))
print('-'*130)


print('thank you')
print('visit again.... ')