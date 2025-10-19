A, B, C, N = (map(int, input().strip().split(" ")))

if 0 <= A <= 10**3 and 0 <= B <= 20**4 and 0 <= C <= 30**5 and 1 <= N <= 10**7:
    print((A**(B**C)) % (N + 1))
else:
    print("Melampaui batas")

