def match_ends(words):
    count=0
    for x in words:
        if (len(x)>=2) and (x[0]==x[len(x)-1]):
            count+=1
    return count

res1=match_ends(['aaa', 'be', 'abc', 'hello'])
print(res1)

def front_x(words):
    # +++your code here+++
    list1=[]
    list2=[]
    for x in words:
        if x[0]=='x':
            list1.append(x)
        elif x[0]!='x':
            list2.append(x)
    a=sorted(list1)
    b=sorted(list2)
    final=a+b
    return final
res2=front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
print(res2)

def value(item):
    return item[-1]
def sort_last(tuples):
  # +++your code here+++
    a=sorted(tuples,key=value)
    return a

res3=sort_last([(1, 1), (1, 3), (3, 4, 5), (2, 2)])
print(res3)