def digitRoot(number):
    digs=[int(char) for char in str(number)]  
    print('digs is',digs)
    out=sum(digs)
    print('the sum of the digits of',number,'is',out)
    return out
def digitRootSort(a):
  first=sorted(a)
  out=sorted(first,key=digitRoot)
  #print('out is',out)
  return out