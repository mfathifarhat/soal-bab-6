N = int(input("Masukkan bilangan bulat :\n"))

if 1 <= N <= 100000:
    
    listBilangan = [int(input().strip()) for _ in range(N)]

    melewatiBatasan = False
    
    for i in listBilangan:
        if i < 1 or i > 100:
            melewatiBatasan = True

    if melewatiBatasan == False:
        listBilangan.sort()

        if (len(listBilangan) % 2 != 0):
            print(f"Median : {listBilangan[(len(listBilangan)//2)]}")
        else:
            print(f"Median : {(listBilangan[(len(listBilangan)//2)] + listBilangan[((len(listBilangan)//2) - 1)]) / 2}")
    else :
        print("Melampaui batasan")
        
else :
    print("Melampaui batasan")