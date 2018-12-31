import sys
import io
import time
import pprint

input_txt = """
4 972439611840
"""

sys.stdin = io.StringIO(input_txt);input()
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import math
from collections import defaultdict

def prime_factorize(n: int):
    prime_factors = defaultdict(int)

    for i in range(2, int(math.sqrt(n)) + 1):
        while True:
            div, mod = divmod(n, i)
            if mod == 0:
                prime_factors[i] += 1
                n = div
            else:
                break
        if n == 1:
            break
    if n != 1:
        prime_factors[n] = 1

    return prime_factors


def main():
    N, P = map(int, input().split())
    prime_factors = prime_factorize(P)

    gcd = 1
    for k, v in prime_factors.items():
        v_cnt = v // N
        gcd *= pow(k, v_cnt)

    print(gcd)
    return

main()
# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__