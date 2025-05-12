n = int(input())
arr = list(map(int, input().split()))

used = set()
arr.sort(reverse=True)  
for x in arr:
    while x > 0:
        if x not in used:
            used.add(x)
            break
        x //= 2

print(len(used))