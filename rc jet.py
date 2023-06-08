jenis_bahan = ["MPPF FORM 5x1000x900mm","control horn 10 set","push rod wire 10 set","brushless motor","linkage stopper","ESC SW50A","receiver iA108 RX","carbon fiber rod 3mm 16 set","servo 9g","rc lipo battery","propeller","flysky-16x remote control"]
harga_bahan = [23,3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]

print("SELAMAT DATANG KE KEDAI UNTUK MEMBELI BARANG UNTUK MEMBUAT RC JET")
print("HARGA barang MPPF FORM 5x1000x900mm=RM23,CONTROL HORN 10 SET=RM3,PUSH ROD WIRE 10 SET=RM2,BRUSHLESS MOTOR=RM15.79,LINKAGE STOPPER 12 SET=RM12,ESC SW50A=RM67,RECEIVER IA108 RX=RM61,CARBON FIBER ROD 3MM 16 SET=RM25.30,SERVO 9G=RM5.20,RC LIPO BATTERY=RM57.56,PROPELLER=RM5.50,FLYSKY-16X REMOTE CONTROL=RM161")
a=int(input("Masukkan tempahan untuk mppf form 5x1000x900mm:"))
b=int(input("Masukkan tempahan untuk control horn 10 set:"))
c=int(input("Masukkan tempahan untuk push rod wire 10 set:"))
d=int(input("Masukkan tempahan untuk brushless motor:"))
e=int(input("Masukkan tempahan untuk linkage stopper 12 set:"))
f=int(input("Masukkan tempahan untuk ESC SW50A:"))
g=int(input("Masukkan tempahan untuk receiver IA108 RX:"))
h=int(input("Masukkan tempahan untuk carbon fiber rod 3mm 16 set:"))
i=int(input("Masukkan tempahan untuk servo 9g:"))
j=int(input("Masukkan tempahan untuk rc lipo battery:"))
k=int(input("Masukkan tempahan untuk propeller:"))
l=int(input("Masukkan tempahan untuk flysky-16x remote control:"))

tempahan = [a,b,c,d,e,f,g,h,i,j,k,l]

def jumlah_harga():
    for i in range(12):
        jumlah[i] = harga_bahan[i]*tempahan[i]
    return(jumlah)

def cetak():
    print("\n\nTempahan anda ialah:")
    print(a,"bahan", jenis_bahan[0])
    print(b,"bahan", jenis_bahan[1])
    print(c,"bahan", jenis_bahan[2])
    print(d,"bahan", jenis_bahan[3])
    print(e,"bahan", jenis_bahan[4])
    print(f,"bahan", jenis_bahan[5])
    print(g,"bahan", jenis_bahan[6])
    print(h,"bahan", jenis_bahan[7])
    print(i,"bahan", jenis_bahan[8])
    print(j,"bahan", jenis_bahan[9])
    print(k,"bahan", jenis_bahan[10])
    print(l,"bahan", jenis_bahan[11])

    print("/nJumlah harga untuk semua bahan yang diperlukan ialah RM",sum (jumlah))
jumlah_harga()
cetak()
print("TERIMA KASIH KERANA MEMBELI BARANG DARI KEDAI KAMI")