#2.soru:
def pisayisi():
    x=[]

    for i in range(1,100000):
        pi=(6/i**2)
        x.append(pi**1/2)
    print(sum(x))

pisayisi()
