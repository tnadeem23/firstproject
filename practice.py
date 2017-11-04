shows=["Got","Sherlock","Breaking bad","Mindhunter"]
print(shows[-1])
shows[2]=23
print(shows[2])
shows.append("House of Cards")
print(shows)
shows.insert(2,"Taboo")
print(shows)
shows.__delitem__(0)
print(shows)
del shows[1]
print(shows)
shows.pop(1)
print(shows)
shows.remove("Mindhunter")
print(shows)
shows.append("Bbc")
#shows.sort(reverse=True)
shows.reverse()
print(shows)
#print(shows.__len__())
print(len(shows))
for x in range(2):
    print(shows[x])
shows2=shows[:]#Makes only a copy rather than equating the both
print(shows2)