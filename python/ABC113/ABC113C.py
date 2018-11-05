import sys
import io

input_txt = """
2 3
1 32
2 63
1 12
"""

sys.stdin = io.StringIO(input_txt)
print(input())

# copy the below part and paste to the submission form.
# ---------function------------
import sys


def main():
    n, m = map(int, input().split())
    lines = sys.stdin.readlines()

    cities = {}
    for i in range(m):
        p, y = map(int, lines[i].split())
        if p in cities:
            cities[p].append((i, y))
        else:
            cities[p] = [(i, y)]

    outputs = [None] * m
    for pref, city_list in cities.items():
        city_list.sort(key=lambda x: x[1])
        # print(pref, city_list)
        city_no = 1
        for city in city_list:
            outputs[city[0]] = "{:06d}{:06d}".format(pref, city_no)
            city_no += 1

    for output in outputs:
        print(output)
    return


main()
# -----------------------------
sys.stdin = sys.__stdin__
