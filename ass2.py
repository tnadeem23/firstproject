def verbing(s):
  # +++your code here+++
    lenstr=len(s)
    if lenstr>=3:
        if s[lenstr-3:lenstr]!='ing':
            s=s+'ing'
            return s
        elif s[lenstr-3:lenstr]=='ing':
            s=s+'ly'
            return s
    else:
        return s
res1=verbing("Talhaing")
print(res1)

def not_bad(s):
  str1=int(s.index('not'))
  str2=int(s.index('bad'))
  if str1<str2:
      new=s.replace(s[str1:str2+3],'good')
      return new
  else:
      return s
res2=not_bad("This food is bad not")
print(res2)

def front_back(a, b):
  len1=len(a)
  len2=len(b)
  if (len1%2)==0:
      len3=int(len1/2)
      afront=a[0:len3]
      aback=a[len3:len1]
  else:
      len3 = int(len1 / 2)
      afront = a[0:len3+1]
      aback = a[len3+1:len1]

  if (len2%2)==0:
      len4=int(len2/2)
      bfront=b[0:len4]
      bback=b[len4:len2]
  else:
      len4 = int(len2 / 2)
      bfront = b[0:len4+1]
      bback = b[len4+1:len2]

  finalstr=afront + bfront + aback + bback
  return finalstr
res3=front_back("Talha","Nadeem")
print(res3)