n, k = map(int, input().split())
while n >= k:
    while n % k != 0:
        n -= 1
        print(n)

    n = n // k
    print(n)
while n > 1:
    n -= 1
    print(n)

