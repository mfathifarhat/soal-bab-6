N = int(input().strip())

if 1 <= N <= 50 :

    strings = [input().strip() for _ in range(N)]

    terpanjang = []
    
    melewatiBatasan = False
    
    for i in strings:
        if 1 <= len(i) <= 50: melewatiBatasan = False
        else : melewatiBatasan = True

    if melewatiBatasan == False:
        for i in strings:
            panjang = 0
            frekuensi = {}
            isGanjil = False
            
            for s in i:
                if s in frekuensi:
                    frekuensi[s] += 1
                else:
                    frekuensi[s] = 1
            
            for a in frekuensi.values():
                if a % 2 == 0:
                    panjang += a
                else:
                    panjang += (a - 1)
                    isGanjil = True
                    
            if isGanjil == True:
                panjang += 1
                    
            terpanjang.append(panjang)
            
        for i in terpanjang:
            print(i)
    else :
        print("Melampaui batas")
else :
    print("Melampaui batas")