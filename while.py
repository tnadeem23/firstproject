flag=True
while flag==True:
    name = input("Enter your name: ")
    if name!='Talha':
        print("Wrong name")
        flag=False
    else:
        print("Welcome "+name)