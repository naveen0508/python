#We have a list of numbers, and we want to group them by the number of digits:

numbers = [1,256,64,65536,186000,1024,8,16,1905]

d = {}

for n in numbers:
  d.setdefault(len(str(n)), []).append(n)

print(d)
