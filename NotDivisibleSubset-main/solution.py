def nonDivisibleSubset(k, s):
    count=[0 for i in range(k)]
    for i in s:
        count[i%k]+=1
    final=0
    if (k % 2 == 0):
        count[k//2] = min(count[k//2], 1)
    if count[0]!=0:
            final+=1
    f=1
    while f<=len(count)//2 :
        final+=max(count[f],count[k-f])
        f+=1
    return(final)