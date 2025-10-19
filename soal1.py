bilanganBulat = int(input("Masukkan bilangan bulat :\n"))

count = 0
listBilangan = []
while count < bilanganBulat:
    count += 1
    listBilangan.append(float(input("Nilai kualitas baju :")))

listBilangan.sort()

if (len(listBilangan) % 2 != 0):
    print(listBilangan[(len(listBilangan)//2)])
else:
    print((listBilangan[(len(listBilangan)//2)] + listBilangan[((len(listBilangan)//2) - 1)]) / 2)