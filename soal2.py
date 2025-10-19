N = int(input("Bilangan bulat"))

frekuensi = [int(input().strip()) for _ in range(N)]

def fpb(a,b):
    if (a % b == 0):
        return b
    else:
        return fpb(b, a % b)

faktorisasi = []

hasilFpb = frekuensi[0]
hasilKali = 1

for i in range(1, len(frekuensi)):
    hasil = fpb(hasilFpb, frekuensi[i])
    
for i in frekuensi:
    hasilKali *= i  
    
print(hasilKali/hasilFpb)