menu={1:"Dosa",2:"Idli",3:"Pulav",4:"Puri",5:"Poha",5:"Upma"}
print('Welcome to our hotel')
print('Menu:\n1:Dosa\n2:Idli\n3:Pulav\n4:Puri\n5:Poha\n5:Upma')
fud_num=int(input('Enter your food number:'))
food=menu.get(fud_num,'invalid_choice')
if food=='invalid_choice':
    print("Sorry Mam we does not have the food item you\'ve chosen" )
else:
    print(f'Mam,here is ur tasty {food}')
