def table():
    num=int(input("Enter number: "))
    rngstr=int(input("Enter range start: "))
    rngend=int(input("Enter range end: "))

    for x in range(rngstr,rngend+1):
        new=num*x
        print(str(num)+" * "+str(x)+" = "+str(new))

def fact():
    num=int(input("Enter number: "))
    for x in range(1,num):
        num=x*num
    print(num)

def power():
    num=int(input("Enter number: "))
    num2=int(input("Enter power: "))
    new=num**num2
    print(new)

def evenodd():
    num=int(input("Enter number: "))
    if num%2==0:
        print("Even")
    else:
        print("Odd")

choice = input("1 - Factorial - 2 Power - 3 Table - 4 Even/Odd: ")
if choice == "1":
    fact()
elif choice == "2":
    power()
elif choice == "3":
    table()
elif choice == "4":
    evenodd()
else:
    print("Wrong Choice!")

#numbers=list(range(1,10,2))
#print(min(numbers))
#print(sum(numbers))