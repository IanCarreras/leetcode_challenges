def uncover_spy(n, trust):
    trusts = {}
    trusted = {}
    
    for p in trust:
        if p[0] in trusts:
            trusts[p[0]] += 1
        else:
            trusts[p[0]] = 1
            
        if p[1] in trusted:
            trusted[p[1]] += 1
        else:
            trusted[p[1]] = 1

    for p in trusted:
        if p not in trusts and trusted[p] + 1 == n:
            return p
        else:
            return -1