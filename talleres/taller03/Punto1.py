def Torre_Hanoi(Discos, a, b, c):
    if (Discos == 1):       
        print(a + " \u2192 " + c)
    else:
        Torre_Hanoi(Discos-1,a,c,b)
        Torre_Hanoi(1,a,b,c)
        Torre_Hanoi(Discos-1,b,a,c)
        
Torre_Hanoi(5, "Torre1", "Torre2", "Torre3")
