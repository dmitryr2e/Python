n, m, c, k = map(int, input().split())

need = n * m - k
if need <= 0:
    print(0)
else:
    packs = (need + 199) // 200
    print(packs * c)
