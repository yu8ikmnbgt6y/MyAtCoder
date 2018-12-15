import sys
import io
import time
import pprint

input_txt = """
6
2 2 2 2 4 4 
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import math
from collections import defaultdict

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    nums_cnt = defaultdict(int)
    for num in nums:
        nums_cnt[num] += 1

    cnt = 0
    for num in reversed(nums):
        if nums_cnt[num] <= 0:
            continue

        power_of_2 = 1 << math.ceil(math.log2(num))
        pair = power_of_2 - num

        if pair != 0 and nums_cnt[pair] > 0:
            nums_cnt[pair] -= 1
            nums_cnt[num] -= 1
            cnt += 1
        elif pair == 0 and nums_cnt[num] >= 2:
            nums_cnt[num] -= 2
            cnt += 1

    print(cnt)
    return

main()
# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__