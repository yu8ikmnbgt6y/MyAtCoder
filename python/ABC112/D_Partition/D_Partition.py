import math
N, M = map(int, input().split())


# Exapmle:enum_divisors(10) returns [1,2,5,10]
def enum_divisors(n, reverse=False):
    divisors = []
    # Each divisor has its own pair.
    # So, it is not necessary to calculate up to n.
    # Calculation up to sqrt(n) is enough.
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return sorted(divisors, reverse=reverse)


# The Solution is the maximum among the integers meeting following conditions.
# (1) One of the divisors of M
# (2) <= int(M/N)
divisors = enum_divisors(M, reverse=True)
divisors = list(filter(lambda x: x <= M//N, divisors))

print(divisors[0])
