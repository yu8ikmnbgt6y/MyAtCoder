import sys
import io

input_txt = """
4 54
"""

sys.stdin = io.StringIO(input_txt)
print(input())

# copy the below part and paste to the submission form.
# ---------function------------
def main():
    x, y = map(int, input().split())
    print(x + y//2)


main()
# -----------------------------
sys.stdin = sys.__stdin__
