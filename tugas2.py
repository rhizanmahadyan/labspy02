R = int(input("Input bilangan ke 1:"))
H = int(input("Input bilangan ke 2:"))
I = int(input("Input bilangan ke 3:"))

if R > H and R > I:
    print("Bilangan / Angka terbesar adalah:", R)
elif H > R and H > I:
    print("Bilangan / Angka terbesar adalah:", H)
else:
    print("Bilangan / Angka terbesar adalah:", I)
    
