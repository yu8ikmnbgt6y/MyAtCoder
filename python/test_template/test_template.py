import sys


def main():
    # ---------function------------
    N, T = map(int, input().split())

    cost = 100001
    for i in range(N):
        ci, ti = map(int, input().split())
        if ti <= T:
            if cost > ci:
                cost = ci
    if cost != 100001:
        print(cost)
    else:
        print('TLE')
    # -----------------------------
    return 0


fname = 'test/input_sample_1.txt'
with open(fname, 'r') as fin:
    sys.stdin = fin
    # メイン関数
    main()


sys.stdin = sys.__stdin__
