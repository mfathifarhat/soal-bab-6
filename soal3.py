N = int(input("Bilangan bulat :"))

skor = []
kemungkinan = []

for i in range(N):
    skorGrup = []
    for a in input().strip().split(" "):
        skorGrup.append(int(a))
    skor.append(skorGrup)
    
for i in skor:
    mungkin = "YES"
    if sum(i[1:]) > ((i[0] * (i[0] - 1) / 2) * 3) or sum(i[1:]) < ((i[0] * (i[0] - 1))):
        mungkin = "NO"
    elif i[1:].count(((i[0] - 1) * 3)) > 1 or i[1:].count(0) > 1:
        mungkin = "NO"
        
    for a in range(1, len(i)):
        if i[a] > ((i[0] - 1) * 3) or i[a] < 0:
            mungkin = "NO"
    kemungkinan.append(mungkin)
    
for i in kemungkinan:
    print(i)