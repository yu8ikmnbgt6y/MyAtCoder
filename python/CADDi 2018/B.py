import sys
import io
import time
import pprint

input_txt = """
10 587586158 185430194
894597290 708587790
680395892 306946994
590262034 785368612
922328576 106880540
847058850 326169610
936315062 193149191
702035777 223363392
11672949 146832978
779291680 334178158
615808191 701464268
"""

sys.stdin = io.StringIO(input_txt);input()
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
def main():
    N, H, W = map(int, input().split())
    cnt = 0
    for i in range(N):
        A, B = map(int, input().split())
        if A >= H and B >= W:
            cnt += 1

    print(cnt)
    return

main()
# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__