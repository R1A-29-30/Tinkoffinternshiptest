import math
n = int(input())
a = []
d = []
for _ in range(n):
    ai, di = map(int, input().split())
    a.append(ai)
    d.append(di)
q = int(input())
for _ in range(q):
    k, t = map(int, input().split())
    k -= 1  

    if t <= a[k]:
        print(a[k])
    else:
        intervals = math.ceil((t - a[k]) / d[k])
        next_train = a[k] + intervals * d[k]
        print(next_train)