t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    def repeat(x):
        for i in range(len(s)):
            if s[i] == "L":
                x -= 1
            elif s[i] == "R":
                x += 1

            if x == 0:
                return i + 1
        return 0   

    z = repeat(x)

    if z == 0 or z > k:
        print(0)
        continue

    res = 1
    rem = k - z
    cycle = repeat(0)

    if cycle == 0:
        print(res)
    else:
        res += rem // cycle
        print(res)
