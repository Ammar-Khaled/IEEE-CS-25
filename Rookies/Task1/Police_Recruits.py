n = int(input())
events = list(map(int, input().split()))
policemen = 0
crimes = 0
for i in range(n):
    if events[i] == -1:  # crime
        if policemen == 0:
            crimes += 1
        else:
            policemen -= 1
    else:
        policemen += events[i]

print(crimes)