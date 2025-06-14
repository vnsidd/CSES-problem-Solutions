def number_spiral(y, x):
    n = max(y, x)
    base = n * n

    if n % 2 == 0:
        if y == n:
            return base - (x - 1)
        else:
            return (n - 1) * (n - 1) + y
    else:
        if x == n:
            return base - (y - 1)
        else:
            return (n - 1) * (n - 1) + x


t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    print(number_spiral(y, x))
