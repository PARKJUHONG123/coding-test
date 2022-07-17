import sys
L = int(sys.stdin.readline().rstrip())
A = sys.stdin.readline().rstrip()

SAME_COUNT_FROM_ZERO_INDEX = [0 for _ in range(L)]

prefix_end_index = 0
for suffix_end_index in range(1, L):
    while prefix_end_index > 0 and A[suffix_end_index] != A[prefix_end_index]:
        prefix_end_index = SAME_COUNT_FROM_ZERO_INDEX[prefix_end_index - 1]

    if A[suffix_end_index] == A[prefix_end_index]:
        prefix_end_index += 1
        SAME_COUNT_FROM_ZERO_INDEX[suffix_end_index] = prefix_end_index

print(L - SAME_COUNT_FROM_ZERO_INDEX[-1])