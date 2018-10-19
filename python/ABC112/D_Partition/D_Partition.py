import math
N, M = map(int, input().split())


def enum_divisors(n, reverse=False):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return sorted(divisors, reverse=reverse)
 
 
divisors = enum_divisors(M, reverse=True)
divisors = filter(lambda x: x <= M//N, divisors)
 
for cand in divisors:
    if M % cand == 0:
        print(cand)
        exit()