def reverse(input):
  return ''.join([input[i] for i in range(len(input)-1, -1,-1)])
s = 'reverse'
print(reverse(s))

# Approach 2
def reverse2(inp):
  l = list(inp)
  l = reversed(l)
  return ''.join(l)
  
s = 'reverse'
print(reverse2(s))
