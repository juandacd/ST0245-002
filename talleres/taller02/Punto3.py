def Subconjuntos(vaina_rara):
    SubconjuntosBase("", vaina_rara)

def SubconjuntosBase(base, s):
    if(len(s) == 0):
        print(base)
    else:
        x = s[1:]
        y= s[:1]
        SubconjuntosBase(base+y,x)
        SubconjuntosBase(base,x)

print(Subconjuntos("ESK9"))
