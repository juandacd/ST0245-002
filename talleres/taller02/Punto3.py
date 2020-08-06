def subconjuntos(vaina_rara):
    subconjuntosBase("", vaina_rara)

def subconjuntosBase(base, s):
    if len(s) == 0:
        print(base)
    else:
        x = s[1:]
        y= s[:1]
        subconjuntosBase(base+y,x)
        subconjuntosBase(base,x)

print(subconjuntos("ESK9"))
