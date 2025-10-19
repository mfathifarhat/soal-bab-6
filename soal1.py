N = int(input("Masukkan bilangan bulat :\n"))

listBilangan = [int(input().strip()) for _ in range(N)]

listBilangan.sort()

if (len(listBilangan) % 2 != 0):
    print(listBilangan[(len(listBilangan)//2)])
else:
    print((listBilangan[(len(listBilangan)//2)] + listBilangan[((len(listBilangan)//2) - 1)]) / 2)