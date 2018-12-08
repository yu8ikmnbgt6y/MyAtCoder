import sys
import io
import time
import pprint

input_txt = """
5 3
5
7
5
7
7
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys
n, k = map(int, input().split())
lines = sys.stdin.readlines()
trees = [None] * n
for i in range(n):
    trees[i] = int(lines[i])

trees.sort()

#print(trees)
min_h = sys.maxsize
k_1 = k - 1
for i in range(n-k+1):
    height_diff = trees[i + k_1] - trees[i]
    if height_diff < min_h:
        min_h = height_diff


print(min_h)

# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__