import sys
import io
import time
import pprint

input_txt = """
2
1
2
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys

def main():
    n = int(input())

    def mod2(str_n):
        return int(str_n) % 2

    has_odd = any(map(mod2, sys.stdin.readlines()))

    if has_odd:
        print('first')
    else:
        print('second')
    return


main()
# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__