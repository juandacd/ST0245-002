def gcd(p,q): 
    if q == 0:
        return p
    else:
        return gcd(q, p % q)
