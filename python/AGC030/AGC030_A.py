import sys
import io
import time
import pprint

input_txt = """
8 8 1
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
def main():
    a, b, c = map(int, input().split())

    ret = 0
    if c <= (a + b + 1):
        ret = b + c
    else:
        ret = b + (a+b+1)
    print(ret)
    return

main()
# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__