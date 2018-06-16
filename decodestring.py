def decodeString(s):
  while processOneBlock(s)!='DONE':
    #print('s started this as',s)
    s=processOneBlock(s)
    #print('s is',s)
  return s

def processOneBlock(s):
  if '[' not in s:
    return 'DONE'
  i=s.rfind('[') #identifies the right-most (interior-most) instance of a character in a string
  mult=s[i-1]
  #print('multiplier is',mult)
  p=i-1
  while True:
    if s[p-1] in [str(q) for q in range(10)]:
      mult=s[p-1]+mult
      p-=1
    else:
      break
  block=s[i+1:(s[i+1:].index(']')+i+1)]
  #print('block to repeat is',block)
  before=s[:i-len(mult)]
  #print('before is',before)
  filler=int(mult)*block
  #print('filler is',filler)
  after=s[i+len(mult)+len(block)+1:]
  #print('after is',after)
  out=before+filler+after
  print('out is',out)
  return out