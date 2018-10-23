import sys
import os


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


input_sample_filename = 'IOset/input_sample_1.txt'
output_sample_filename = 'IOset/output_sample_1.txt'
tmpfname = 'tmpfile'

with open(input_sample_filename, 'r') as fin, open(tmpfname, 'w') as fout:
    sys.stdin = fin
    sys.stdout = fout
    # メイン関数
    main()

# 後処理
sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__

# 検証
with open(tmpfname, 'r') as src, open(output_sample_filename, 'r') as tgt:
    for line1, line2 in zip(src, tgt):
        line1, line2 = map(lambda x: x.rstrip(), [line1, line2])
        print(line1, line2, line1 == line2)
os.remove(tmpfname)
