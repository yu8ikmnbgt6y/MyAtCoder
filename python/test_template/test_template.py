import sys
import io

input_txt = """
3 70
7 60
1 80
4 50
"""

sys.stdin = io.StringIO(input_txt)
print(input())

# copy the below part and paste to the submission form.
# ---------function------------
def main():
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

    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
