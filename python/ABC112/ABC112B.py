N, T = map(int, input().split())

cost = None
for i in range(N):
    ci, ti = map(int, input().split())
    if ti <= T:
        if cost > ci:
            cost = ci
if cost:
    print(cost)
else:
    print('TLE')