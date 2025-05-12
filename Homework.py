def min_cost_to_make_valid(a, b, s):
    balance = 0
    cost = 0
    for ch in s:
        if ch == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                cost += min(a, 2 * b)
                balance = 0
    cost += balance * b
    return cost

a, b, = map(int, input().split())
s = input().strip()

print(min_cost_to_make_valid(a, b, s))