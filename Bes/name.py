# useful function
def name(dsts,m):
    name=[]
    N=len(dsts)
    for i in range(0,N):
        s=dsts[i].split('/')
        name.append('')
        name[i] =s[-1]
        for j in range(2,m+1):
            name[i] =name[i]+'_'+s[-j]
    return name
def getname(dsts):
    i=1
    while 1:
        nm0 = name(dsts,i)
        s=set(nm0)
        if len(s)== len(dsts) :
            return nm0
        else:
            i = i+1
            nm0=name(dsts,i)
