sentence='The Mississippi River'
def count_chars(s):
  s = s.lower()
  count=list(map(s.count,s))
  return (max(count))
  
print(count_chars(sentence))


# Approach 2

sentence='The Mississippi River'
def count_char(s):
  s=s.lower()
  L = [s.count(c) for c in s]
  return max(L)
print (count_char(sentence))


# Approach 3

sentence='The Mississippi River'
sl = sentence.lower()
d = {}.fromkeys([x for x in sl],0)
for char in sl:
  d[char] += 1
print(d)

# Approach 4

sentence='The Mississippi River'
sl = sentence.lower()
d = {}
for c in sl:
  d[c] = d.get(c,0) + 1
print(d)


# Approach 5

sentence = "The Mississippi River"
ans = dict((c,sentence.count(c)) for c in sentence)
print(ans)