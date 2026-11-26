a, b, c = map(int, input().split())

if a > b:
    a, b = b, a

if c < a:
    print(a - c)
elif c > b:
    print(c - b)
else:
    print(0)
