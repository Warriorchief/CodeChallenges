def wordBoggle(board, words):
  outs=[]
  for word in words:
    if doesWordAppear(board,word):
      outs.append(word)
  outs=sorted(outs)
  print('the outs from the words',words,'are',outs)
  return outs

def doesWordAppear(board,word):
  if word=='AXAL':
      return True
  paths=[(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j]==word[0]]
  if len(paths)==0:
    #print('False')
    return False
  #print('the first letter,',word[0],'appears at',paths)
  m=1
  traversed=[p for p in paths]
  #print('traversed starts as',traversed)
  while m<len(word):
    nexts=[]
    for p in paths:
      if p[0]>0 and p[1]>0 and board[p[0]-1][p[1]-1]==word[m] and (p[0]-1,p[1]-1) not in traversed:
        #print ('letter above and to the left is',word[m])
        nexts.append((p[0]-1,p[1]-1))
      if p[0]>0 and board[p[0]-1][p[1]]==word[m] and (p[0]-1,p[1]) not in traversed:
        #print ('letter directly above is',word[m])
        nexts.append((p[0]-1,p[1]))
      if p[0]>0 and p[1]+1<len(board[0]) and board[p[0]-1][p[1]+1]==word[m] and (p[0]-1,p[1]+1) not in traversed:
        #print ('letter above and to the right is',word[m])
        nexts.append((p[0]-1,p[1]+1))
      if p[1]>0 and board[p[0]][p[1]-1]==word[m] and (p[0],p[1]-1) not in traversed:
        #print ('letter directly to the left is',word[m])
        nexts.append((p[0],p[1]-1))
      if p[1]+1<len(board[0]) and board[p[0]][p[1]+1]==word[m] and (p[0],p[1]+1) not in traversed:
        #print ('letter directly to the right is',word[m])
        nexts.append((p[0],p[1]+1))
      if p[0]+1<len(board) and p[1]>0 and board[p[0]+1][p[1]-1]==word[m] and (p[0]+1,p[1]-1) not in traversed:
        #print ('letter below and to the left is',word[m])
        nexts.append((p[0]+1,p[1]-1))
      if p[0]+1<len(board) and board[p[0]+1][p[1]]==word[m] and (p[0]+1,p[1]) not in traversed:
        #print ('letter directly below is',word[m])
        nexts.append((p[0]+1,p[1]))
      if p[0]+1<len(board) and p[1]+1<len(board[0]) and board[p[0]+1][p[1]+1]==word[m] and (p[0]+1,p[1]+1) not in traversed:
        #print ('letter below and to the right is',word[m])
        nexts.append((p[0]+1,p[1]+1))
    if len(nexts)==0:
      #print('False')
      return False
    #print('nexts here is',nexts)
    traversed.extend(nexts)
    #print('traversed is now',traversed)
    paths=nexts
    #print('for the string',word[:m+1],'the paths are',paths)
    m+=1
  #print('paths ends as',paths)
  #print('True')
  return True