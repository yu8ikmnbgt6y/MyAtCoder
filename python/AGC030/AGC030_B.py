import sys
import io
import time
import pprint

input_txt = """
314159265 7
21662711
77271666
89022761
156626166
160332356
166902656
298992265
"""

sys.stdin = io.StringIO(input_txt);input()
#sys.stdin = open('in.test')
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
import sys

def main():
    L, N = map(int, input().split())
    lines = sys.stdin.readlines()

    trees_ccw = [None] * N
    trees_ccw = [int(lines[i]) for i in range(N)]
    trees_cw = [L - trees_ccw[-(i+1)] for i in range(N)]
    trees_ccw_accum = [0] + [None] * N
    trees_cw_accum = [0] + [None] * N
    for i in range(N):
        trees_ccw_accum[i+1] = trees_ccw_accum[i] + trees_ccw[i]
        trees_cw_accum[i+1] = trees_cw_accum[i] + trees_cw[i]

    #print(trees_ccw)
    #print(trees_cw)
    #print(trees_ccw_accum)
    #print(trees_cw_accum)

    dist_max = 0

    for offset in range(1, N+1):
        remain = N - offset
        n_left = offset + remain // 2   # the number of times to move the left(counter clockwise)
        n_right = N - n_left            # the number of times to move the right(clockwise)

        print('L' * offset + '_', end='')
        for i in range(N-offset):
            if i % 2 == 0:
                print('R', end='')
            else:
                print('L', end='')
        print()
        #print(offset, n_left, n_right)

        dist_ccw = 2 * (trees_ccw_accum[n_left] - trees_ccw_accum[offset-1]) + 2 * trees_cw_accum[n_right]
        dist_cw = 2 * (trees_cw_accum[n_left] - trees_cw_accum[offset-1]) + 2 * trees_ccw_accum[n_right]

        if remain % 2 == 0:
            dist_ccw -= trees_ccw[n_left-1]
            dist_cw -= trees_cw[n_left-1]
        else:
            dist_ccw -= trees_cw[n_right-1]
            dist_cw -= trees_ccw[n_right-1]

        if dist_max < dist_ccw:
            dist_max = dist_ccw

        if dist_max < dist_cw:
            dist_max = dist_cw

        #print(n_left, dist_1, dist_2, dist_max)

    print(dist_max)
    return

main()
# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__