from infomodule import information as inf
#from infomodule import *
def info(name,gender,age=''):
    person={
        'name':name,
        'gender':gender
    }
    if age:
        person['age']=age
    return person

per1=info("Talha",'Male')
for specs,value in per1.items():
    print(specs+" = "+str(value))

def vehicles(price,*cars):
    for car in cars:
        print("Car = "+car)
        print("Price = "+str(price))

vehicles(2000,"BMW","Lamborghini")



ret=inf("Talha","Nadeem",gender='Male',residence='Pakistan')
print(ret)