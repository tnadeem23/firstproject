# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
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


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  str1=int(s.find('not'))
  str2=int(s.find('bad'))
  if str1<str2:
      new=s.replace(s[str1:str2+3],'good')
      return new
  else:
      return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
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


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
