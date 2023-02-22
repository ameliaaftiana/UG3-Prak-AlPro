#input
dadu1=int(input("dadu1 = "))
dadu2=int(input("dadu2 = "))
dadu3=int(input("dadu3 = "))

#proses
tambah=dadu1+dadu2+dadu3

if tambah == 18:
    print ("Royal")
elif dadu1==dadu2==dadu3:
    print ("Triple")
elif dadu1==4 and dadu2==5 and dadu3==6:
    print("Flush")
elif dadu1==dadu2 or dadu1==dadu3 or dadu2==dadu3:
    print ("Double")
elif dadu1!=dadu2 or dadu1!=dadu3 or dadu2!=dadu3:
    print ("Single")

