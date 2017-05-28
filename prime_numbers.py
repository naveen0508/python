inp = int(input("Enter the number: "))

def isPrime(n):
  if n == 1:
    return False
  for t in range(2,n):
    if n % t == 0:
      return False
  return True
  
print(isPrime(inp))

def primes(n=1):
  while n <= inp:
    if isPrime(n): yield n
    n +=1 

for n in primes():
  print (n)
