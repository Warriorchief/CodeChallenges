import re

#words = ["This", "is", "an", "example", "of", "text", "justification."]
words=["Two", 
 "words."]
l=11

def textJustification(words, l):
  """ if sum([len(w) for w in words])+(len(words)-1)<=l:
        print('this is a single-liner')
        singleLine=''.join(words)
        print('in which case it has to just become',justLine(singleLine,l))
        return justLine(singleLine,l)
  """
  block=[]
  i=0
  while i<len(words):
    if i+1==len(words):
      line=words[i]
      block.append(line)
      break
    line=words[i]
    while True:
      print('i here i is',i,'and line is',line)
      if i+1>len(words)-1:
        break
      if len(line+' '+words[i+1])>l:
        i+=1
        break
      else:
        line+=' '+words[i+1]
        i+=1
    #print('line is',line)
    block.append(line)
    #print('block at 24 is',block)
  out=[justLine(line,l) for line in block]
  #print('out is',out)
  #for o in out:
    #print(o,len(o))
  return out

def justLine(line,l):
  if line.count(' ')==0:
    line=line+((l-len(line))*' ')
    #print('on the one-word line we switched to be',line,'which has length',len(line))
    return line
  spacesNeeded=l-sum([len(g) for g in line.split()])
  numWords=len([g for g in line.split()])
  numGaps=numWords-1
  minFill=spacesNeeded//numGaps
  #print('minFill is',minFill)
  line=re.sub(' ',' '*minFill,line,numGaps)
  #print ('line is now',line)
  if spacesNeeded%numGaps!=0:
    extras=spacesNeeded%numGaps
    #print('the leftover extra spaces is',extras)
    line=re.sub(' '*minFill,' '*(minFill+1),line,extras)
    #print('line just got extras added to become',line)
  #print('line ends as',line,'which has length',len(line))
  return line



print(textJustification(words,l))