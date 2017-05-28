 L = [3,1,5,7,6,4,2,8,10,9]

for j in range(len(L)-1):
  for i in range(len(L)-1):
    if L[i] > L[i+1]:
      temp = L[i]
      L[i] = L[i+1]
      L[i+1] = temp
  print(L)