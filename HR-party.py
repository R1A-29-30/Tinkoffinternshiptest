from itertools import permutations
n = int(input())
heights = list(map(int, input().split()))

heights.sort()
arranged = []
left = 0
right = n - 1
while left <= right:
    if left == right:
        arranged.append(heights[left])
    else:
        arranged.append(heights[left])
        arranged.append(heights[right])
    left += 1
    right -= 1
max_diff = 0
best_order = []
arranged.sort()
for i in range(n):
    if i % 2 == 0:
        best_order.insert(0, arranged[i])
    else:
        best_order.append(arranged[i])
total = 0
for i in range(n - 1):
    total += abs(best_order[i + 1] - best_order[i])

print(total)