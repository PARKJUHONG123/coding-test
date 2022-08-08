import sys
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())

START = ord('a')
words = list()
fix_answer = 0
conf = set(['a', 'n', 't', 'i', 'c'])

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    word = word[4:-4]
    if len(word) == 0:
        fix_answer += 1
    else:
        word_element = set(word) - conf

        if len(word_element) > K - 5:
            continue

        words.append(word_element)

max_answer = 0
if K < 5:
    print(0)
else:
    alpha = set()
    for word in words:
        alpha |= word
    
    alpha_list = list(alpha)

    if len(alpha_list) < K - 5:
        comb = combinations(alpha_list, len(alpha_list))
    else:
        comb = combinations(alpha_list, K - 5)

    for value in comb:
        count = 0
        value = set(value)
        for word in words:
            result = word - value
            if not result:
                count += 1
        max_answer = max(max_answer, count)
    print(max_answer + fix_answer)

'''
K = 2

M
XYZ
YZX
ZXY


'''