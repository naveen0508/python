ss = ''' this is a word count program and this should return
 word count'''

words = ss.split()
d1 = {}.fromkeys(words, 0)
for w in words:
  d1[w] += 1
print(d1)


# second approach

d2 = {}
for w in ss.split():
  d2[w] = d2.get(w,0) + 1
print(d2)

# third approach

from collections import defaultdict

d3 = defaultdict(int)
for w in words:
  d3[w] += 1
print(d3)


# 4th approach

c = 'this this is is a a string'
d = c.split()
e = collections.Counter(d)
print(e)

print([k for k,v in e.items() if v>1]) # to print out the duplicates
