#input
p1=int(input("p1 = "))
p2=int(input("p2 = "))
p3=int(input("p3 = "))

#proses
selp1=p1-21
selp2=p2-21
selp3=p3-21

if p1==21:
    print ("pemenangnya adalah p1")
elif p2==21:
    print("pemenangnya adalah p2")
elif p3==21:
    print("pemenangnya adalah p3")
elif (p1>21 and p2>21 and p3>21) or p1==p2 or p1==p3 or p2==p3:
    print("tidak ada pemenangnya")
elif p1<21 and abs(selp1)<abs(selp2) and abs(selp1)<abs(selp3):
    print("maka pemenangnya adalah p1")
elif p2<21 and abs(selp2)<abs(selp1) and abs(selp2)<abs(selp3):
    print("maka pemenangnya adalah p2")
elif p3<21 and abs(selp3)<abs(selp1) and abs(selp3)<abs(selp2):
    print("maka pemenangnya adalah p3")
