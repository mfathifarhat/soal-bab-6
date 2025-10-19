N = int(input("Bilangan bulat"))

frekuensi = [int(input().strip()) for _ in range(N)]

def fpb(a,b):
    if (a % b == 0):
        return b
    else:
        return fpb(b, a % b)

def kpk(a,b):
    return a * b / fpb(a,b)

hasilKpk = kpk(frekuensi[0], frekuensi[0 + 1])

if len(frekuensi) > 2:
    for i in range(2, len(frekuensi)):
        hasilKpk = kpk(hasilKpk, frekuensi[i])

print(hasilKpk)