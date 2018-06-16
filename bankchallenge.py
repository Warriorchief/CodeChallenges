def bankRequests(accounts, requests):
    for r in requests:
        if len(r.split(' '))==4:
            frm,to,amount=int(r.split(' ')[1]),int(r.split(' ')[2]),int(r.split(' ')[3])
            print('frm,to,amount are',frm,to,amount)
            if frm not in range(1,len(accounts)+1) or to not in range(1,len(accounts)+1):
                fail=requests.index(r)
                return [int('-'+str(fail+1))]     
            if amount>accounts[frm-1]:
                fail=requests.index(r)
                return [int('-'+str(fail+1))]
            accounts[frm-1]-=amount
            accounts[to-1]+=amount
            print('accounts are',accounts)
        if r.split(' ')[0]=='withdraw':
            frm,amount=int(r.split(' ')[1]),int(r.split(' ')[2])
            if frm not in range(1,len(accounts)+1):
                fail=requests.index(r)
                return [int('-'+str(fail+1))] 
            print('frm,amount are',frm,amount)
            if amount>accounts[frm-1]:
                fail=requests.index(r)
                return [int('-'+str(fail+1))]
            accounts[frm-1]-=amount
            print('accounts are',accounts)
        if r.split(' ')[0]=='deposit':
            to,amount=int(r.split(' ')[1]),int(r.split(' ')[2])
            if to not in range(1,len(accounts)+1):
                fail=requests.index(r)
                return [int('-'+str(fail+1))] 
            print('to,amount are',to,amount)
            accounts[to-1]+=amount
            print('accounts are',accounts)
    return accounts