import string
alph=string.ascii_uppercase
def newNumeralSystem(number):
  number=alph.index(number)
  print('number is now',number)
  out=[]
  pairs=[[i,number-i] for i in range(int(number//2)+1)]
  print('the number',number,'can be summed as the pairs',pairs)
  for p in pairs:
    q=str(alph[p[0]])+' + '+str(alph[p[1]])
    out.append(q)
  print('out is',out)
  return out