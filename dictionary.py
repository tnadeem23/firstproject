car={'name':'Bmw' ,'price':'100000' ,'type':'sssedan'}

print(car['name'])

car['model']=2010
print(car['model'])
print(car['name'])

if car['type']=='luxury':
    car['price']=int(car['price'])+5000
    print(car['price'])
elif car['type']=='sedan':
    car['price']=car['price']
    print(car['price'])
else:
    print('No such type exists')

for key,value in car.items():
    print("Key = "+str(key))
    print("Value = "+str(value))

renownedcars=['Ferrari','Lamborghini','Bmw']
for cars in car.values(): #set() for no repition
    print(cars.title())
    if cars in renownedcars:
        print(cars+" is my fav car")