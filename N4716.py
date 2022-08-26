import sys

while True:
    left, right = list(), list()
    N, A, B = map(int, sys.stdin.readline().split())
    if N == 0 and A == 0 and B == 0:
        break

    for _ in range(N):
        K, DA, DB = map(int, sys.stdin.readline().split())

        if DA > DB:
            left.append([K, DA, DB])
        else:
            right.append([K, DA, DB])    

    answer = 0
    for SK, SA, SB in right: 
        answer += SK * SA
        A -= SK

    for SK, SA, SB in left:
        answer += SK * SB
        B -= SK

    while A < 0:
        leftover = -A
        for RK, RA, RB in sorted(right, key = lambda x : x[2] - x[1]):
            if RK >= leftover:
                answer += (RB - RA) * leftover
                A += leftover
                break
            else:
                answer += (RB - RA) * (RK)
                leftover -= RK
                A += RK

    while B < 0:
        leftover = -B
        for LK, LA, LB in sorted(left, key = lambda x : x[1] - x[2]):
            if LK >= leftover:
                answer += (LA - LB) * leftover
                B += leftover
                break
            else:
                answer += (LA - LB) * (LK)
                leftover -= LK
                B += LK

    print(answer)