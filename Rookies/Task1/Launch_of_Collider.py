n = int(input())
dirs = input()
x = list(map(int, input().split()))

ans = 1e9
r = l = -1

for i in range(n):
    if dirs[i] == 'R':
        r = x[i]
    else:
        if r != -1:
            ans = min(ans, (x[i] - r) // 2)

print(ans if ans != 1e9 else -1)