import sys
import io
import time
import pprint

input_txt = """
BBW
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
def main():
    txt = input()

    w_cnt = 0
    cnt = 0
    for char in reversed(txt):
        if char == 'W':
            w_cnt += 1
        else:
            cnt += w_cnt
    print(cnt)
    return

main()
# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__