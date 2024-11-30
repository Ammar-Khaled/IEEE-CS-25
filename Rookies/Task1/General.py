n = int(input())
heights = list(map(int, input().split()))
max_element = 0
max_index = 0
min_element = 101
min_index = 0

for i in range(n):
    if heights[i] > max_element:
        max_element = heights[i]
        max_index = i

    if heights[i] <= min_element:
        min_element = heights[i]
        min_index = i

ans = (max_index - 0) + (n - 1 - min_index)
if max_index > min_index:
    ans -= 1

print(ans)
