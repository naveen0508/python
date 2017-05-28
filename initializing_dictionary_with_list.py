cities = {'San Francisco': 'US', 'London':'UK',
'Manchester':'UK', 'Paris':'France',
'Los Angeles':'US', 'Seoul':'Korea'}

# => {'US':['San Francisco', 'Los Angeles'], 'UK':[,], ...}


# approach 1

from  collections import defaultdict

d1 = defaultdict(list)  # initialize dict with list
for k,v in cities.items():
  d1[v].append(k)
print(d1)

# approach 2
# using dict.setdefault(key, default=None)
d2 = {}
for k,v in cities.items():
  d2.setdefault(v,[]).append(k)
print(d2)


# another example
'''We want to make a dictionary with the number of digits as the key and list of
numbers the value'''

L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]

#from collections import defaultdict
d = defaultdict(list)
for i in L:
  d[len(str(i))].append(i)
print(d)
print ({k:v for k,v in d.items()})
