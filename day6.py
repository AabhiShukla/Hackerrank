TC = input()

for j in range(int(TC)):
  S = input()
  even=[]
  odd=[]
  for i in range(len(S)):
      if i == 0 or (i% 2) == 0:
          even.append(S[i])
      else:
          odd.append(S[i])
  print (''.join(even)+" "+''.join(odd))
