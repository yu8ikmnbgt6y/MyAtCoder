import sys
import io
import time
import pprint

input_txt = """
9592
"""

sys.stdin = io.StringIO(input_txt);input()
start_time = time.time()
# copy the below part and paste to the submission form.
# ---------function------------
def main():
    txt = input()
    print(txt.count('2'))
    return

main()
# -----------------------------
print("elapsed:", time.time() - start_time)
sys.stdin = sys.__stdin__