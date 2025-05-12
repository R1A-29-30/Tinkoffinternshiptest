import math
from functools import reduce
from collections import defaultdict

MOD = 10 ** 9 + 7

def get_divisors(x):
    divs = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.append(i)
            if i != x // i:
                divs.append(x // i)
    return divs

def mobius_sieve(n):
    mu = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i, n + 1, i):
                is_prime[j] = False
                mu[j] *= -1
            j = i * i
            while j <= n:
                mu[j] = 0
                j += i * i
    return mu

def solve(n, A):
    max_a = max(A)
    mu = mobius_sieve(max_a)

    # precompute divisors for all A[i]
    divisors = [get_divisors(a) for a in A]

    # For each possible GCD d, store list of options where each bᵢ divides aᵢ/d
    contrib = defaultdict(int)

    for d in range(1, max_a + 1):
        valid = True
        options = []
        for i in range(n):
            if A[i] % d != 0:
                valid = False
                break
            a_div = A[i] // d
            b_list = get_divisors(a_div)
            beauty_list = []
            for b in b_list:
                x = A[i]
                y = d * b
                g = math.gcd(x, y)
                x //= g
                y //= g
                beauty = (x + y) % MOD
                beauty_list.append(beauty)
            options.append(beauty_list)
        if not valid:
            continue

        # Multiply all possible combinations of beauty values
        total = 1
        for beauty_list in options:
            s = sum(beauty_list) % MOD
            total = (total * s) % MOD

        contrib[d] = total

    # Apply Möbius inversion to get only GCD = 1 sequences
    result = 0
    for d in contrib:
        result = (result + mu[d] * contrib[d]) % MOD

    return result % MOD


# Input handling
n = int(input())
A = list(map(int, input().split()))
print(solve(n, A))