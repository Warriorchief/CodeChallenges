def periodicSequence(s0, a, b, m):
    out=[s0]
    i=1
    while True:
        nxt=(a*out[i-1]+b)%m
        print('nxt is',nxt)
        if nxt in out:
            gap=i-out.index(nxt)
            print('gap is',i-out.index(nxt))
            return gap
        out.append(nxt)
        i+=1
    