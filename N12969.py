import sys

N, K = map(int, sys.stdin.readline().split())

def ABC(n, k):
    a_cnt, b_cnt = 0, 0
    start_index = 1
    ret = ['C' for _ in range(n)]

    if k == 0:
        return ''.join(ret)

    if ret[-start_index] == 'C':
        cur_k = 0
        target_index = start_index 

        while ret[-target_index] == 'C':
            a_cnt += 1
            while ret[-target_index] == 'C':
                ret[-target_index] = 'A'
                if target_index != start_index + a_cnt - 1:
                    ret[-target_index + 1] = 'C'
                    cur_k = cur_k + 1
                target_index += 1
                if k == cur_k:
                    return ''.join(ret)
                if target_index > n:
                    break
            target_index = start_index + (a_cnt)
            if target_index + a_cnt >= n:
                break

            if ret[-(target_index + a_cnt)] == 'A':
                break
    
    if ret[-start_index] == 'C':
        target_index = start_index

        while ret[-target_index] == 'C':
            b_cnt += 1
            while ret[-target_index] == 'C':
                ret[-target_index] = 'B'
                if target_index != start_index + b_cnt - 1:
                    ret[-target_index + 1] = 'C'
                    cur_k += 1
                target_index += 1
                if k == cur_k:
                    return ''.join(ret)
                if target_index > n:
                    break

            target_index = start_index + (b_cnt)

    return -1


print(ABC(N, K))
