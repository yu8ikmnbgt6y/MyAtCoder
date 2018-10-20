num = int(input())
for item in [i*111 for i in range(1, 10)]:
    if num <= item:
        print(item)
        break
