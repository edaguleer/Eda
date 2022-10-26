#9.soru
for k in range(1,1000):
    m=str(k)+"000000"
    if int(m[0])+int(m[1])+int(m[2])<9:
        print(k,end=' ')
