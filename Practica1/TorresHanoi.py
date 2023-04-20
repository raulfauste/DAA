def torres_de_hanoi(n,o,d,a):
    if n == 1:
        print("Mueve disco 1 desde torre",o,"a torre",a)
        print("Mueve disco 1 desde torre",a,"a torre",d)
    else:
        torres_de_hanoi(n-1,o,d,a)
        print("Mueve disco",n, "desde torre",o,"a torre",a)
        torres_de_hanoi(n - 1,d,o,a)
        print("Mueve disco",n, "desde torre",a,"a torre",d)
        torres_de_hanoi(n - 1,o,d,a)

n = int(input())
torres_de_hanoi(n,1,3,2)
