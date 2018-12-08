import sys
import io
import time
import pprint

input_txt = """
999999999
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import itertools
max_753_numbers = {2: 0}
for i in range(3, 10):
    max_753 = pow(3, i) - (3 * pow(2, i) - 3 * pow(1, i))
    max_753_numbers[i] = max_753_numbers[i-1] + max_753


def main():
    n_str = input()
    if len(n_str) <= 2:
        print(0)
        return
    n = int(n_str)

    base_number = max_753_numbers[len(n_str)-1]
    cnt= 0
    for combi in itertools.product('357', repeat=len(n_str)):
        if '3' in combi and '5' in combi and '7' in combi:
            if int(''.join(combi)) <= n:
                cnt += 1

    ans = base_number + cnt
    print(ans)
    return



main()

# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__