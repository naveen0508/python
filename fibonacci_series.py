# recursive
def fibo(n):
  if n == 0 or n ==1:
    return n
  return fibo(n-1) + fibo(n-2)
  

for i in range(10): print(fibo(i))




# iterative
def fibi(n):
  a, b = 0, 1
  for i in range(0,n):
    a, b = b, a+b
  return a