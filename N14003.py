import sys
from bisect import bisect_left
import collections

MIN = -1000000001
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [MIN]
index_dict = collections.defaultdict(list)


for i in range(len(arr)):
    value = arr[i]
    if stack[-1] < value:
        index = len(stack)
        stack.append(value)
        index_dict[index].append(i)

    else:
        index = bisect_left(stack, value)
        stack[bisect_left(stack, value)] = value
        index_dict[index].append(i)

length = len(stack) - 1
ret = list()

max_index = N
for i in reversed(range(1, length + 1)):
    for index in sorted(index_dict[i], reverse=True):
        if index < max_index:
            ret.append(arr[index])
            max_index = index
            break

print(length)
print(*ret[::-1])
