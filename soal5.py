N = int(input().strip())

strings = [input().strip() for _ in range(N)]

matrix = [[i for i in range(len(strings))]]

terpanjang = []

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