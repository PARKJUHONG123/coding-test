import sys

N, M = map(int, sys.stdin.readline().split())

trie = dict()

def make_trie(p_index, p_trie):
    if p_index >= length:
        return
    
    cur_value = value[p_index]
    if cur_value not in p_trie:
        p_trie[cur_value] = dict()
    make_trie(p_index + 1, p_trie[cur_value])

def is_prefix(p_index, p_trie):
    if p_index >= t_length:
        return 1

    cur_value = target[p_index]
    if cur_value not in p_trie:
        return 0
    return is_prefix(p_index + 1, p_trie[cur_value])

for _ in range(N):
    value = sys.stdin.readline().rstrip()
    length = len(value)
    make_trie(0, trie)

ret = 0
for _ in range(M):
    target = sys.stdin.readline().rstrip()
    t_length = len(target)
    ret += is_prefix(0, trie)
print(ret)