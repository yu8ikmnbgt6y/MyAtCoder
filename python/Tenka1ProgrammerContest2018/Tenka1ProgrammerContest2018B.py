def give_cookies(src, dst):
    dst += src // 2
    src = src // 2
    return src, dst


def main():
    A, B, K = map(int, input().split())

    cnt = 0
    while True:
        # From Takahashi to Aoki
        A, B = give_cookies(A, B)
        cnt += 1
        if cnt == K:
            break

        # From Aoki to Takahashi
        B, A = give_cookies(B, A)
        cnt += 1
        if cnt == K:
            break
    print(A, B)
    return


main()
