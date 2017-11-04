persons=[]
for person in range(50):
    persons1={'Name':'Talha' , 'Age':'20' , 'Gender':'Male'}
    persons.append(persons1)

for per in persons[:10]:
    print(per)
    print("Total no of person = "+str(len(persons)))

for pers in persons[0:5]:
    if pers['Name']=='Talha':
        pers['Name']='Hamza'

for perss in persons[0:5]:
    print(perss)