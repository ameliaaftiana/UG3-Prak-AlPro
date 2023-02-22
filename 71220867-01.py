#input
jarak=int(input("Masukkan Jarak = "))
batas=int(input("Masukkan Batas_a = "))
nilai=int(input("Masukkan Nilai = "))

#proses
batas1=batas
batas2=batas1-jarak
batas3=batas2-jarak
batas4=batas3-jarak
batas5=batas4-jarak
batas6=batas5-jarak
batas7=batas6-jarak
batas8=batas7-jarak
batas9=batas8-jarak

if nilai >= batas1:
    print("Maka jawabannya adalah A")
elif nilai >= batas2:
    print("Maka jawabannya adalah A-")
elif nilai >= batas3:
    print("Maka jawabannya adalah B+")
elif nilai >= batas4:
    print("Maka jawabannya adalah B")
elif nilai >= batas5:
    print("Maka jawabannya adalah B-")
elif nilai >= batas6:
    print ("Maka jawabannya adalah C+")
elif nilai >= batas7:
    print ("Maka jawabannya adalah C")
elif nilai >= batas8:
    print ("Maka jawabannya adalah D")
else:
    print ("Maka jawabannya adalah E")

