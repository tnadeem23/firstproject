def donuts(count):
  # +++your code here+++
  if count<10:
    re=print("Number of dounts: "+str(count))
  elif count>10:
    re=print("Number of dounts: "+"many")
  return re
res1=donuts(9)
print(res1)


def both_ends(s):
  # +++your code here+++
  if len(s)>=2:
      str1=s[0:2]
      str2=s[len(s)-2:len(s)]
      new=str1+str2
      return new
  else:
      new=''
      return new
res2=both_ends("TalhaNadeem")
print(res2)

def fix_start(s):
  # +++your code here+++
    stor=list(s)
    occur=stor[0]
    for x in range(0,len(stor)):
        if occur==stor[x]:
            str = '*'
            stor[x] = str
    stor[0]=occur
    a="".join(stor)
    return a
res3=fix_start("TalhaTTal")
print(res3)


def mix_up(a, b):
  # +++your code he
  store1=list(a)
  store2=list(b)
  original=store1[0]
  store1[0]=store2[0]
  store2[0]=original
  a="".join(store1)
  b="".join(store2)
  c=a+" "+b
  return c
res4=mix_up('talha','nadeem')
print(res4)
