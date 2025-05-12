n = int(input())
arr = list(map(int, input().split()))

count = 0

for l in range(n):
    for r in range(l + 2, n):
        sub = arr[l:r+1]
        found = False
        for i in range(len(sub)):
            for j in range(i+1, len(sub)):
                for k in range(j+1, len(sub)):
                    if sub[j]*2 == sub[i] + sub[k]:
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if found:
            count += 1

print(count)