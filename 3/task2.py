t = int(input())

for i in range(t):
    n = int(input())
    p, q = map(int, input().split())
    bits = []
    for j in range(n):
        p *= 2
        bits.append(str(p // q))
        p %= q
    print("0." + "".join(bits))
