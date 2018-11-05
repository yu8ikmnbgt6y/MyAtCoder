import sys
import io

input_txt = """
3
21 -11
81234 94124 52141
"""

sys.stdin = io.StringIO(input_txt)
print(input())

# copy the below part and paste to the submission form.
# ---------function------------
import sys
def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    min_abs = sys.maxsize
    min_abs_idx = -1
    for idx, item in enumerate(h):
        tmp_tmp = t - item * 0.006
        tmp_abs = abs(tmp_tmp - a)
        if tmp_abs < min_abs:
            min_abs = tmp_abs
            min_abs_idx = idx

    print(min_abs_idx + 1)
    return

main()
# -----------------------------
sys.stdin = sys.__stdin__
