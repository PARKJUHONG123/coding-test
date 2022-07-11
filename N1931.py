import sys, collections
N = int(sys.stdin.readline().rstrip())

book_dict = collections.defaultdict(list)

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    book_dict[end].append(start)

# 종료 시간 기준으로 dictionary 생성 (key : value = 종료 시간 : 시작 시간)

ret, cur_end = 0, -1
for end in sorted(book_dict):
    # 종료 시간 기준으로 sorted asc 하게 조회
    for start in sorted(book_dict[end]):
        # 각 종료 시간의 시작 시간을 sorted asc 하게 조회
        if cur_end <= start:
            # 만약에 현재 종료 시점보다 이 다음 스케줄의 시작 시간이 크거나 같을 경우, 다음 스케줄의 종료 시간으로 현재 종료 시점을 변경하고 count += 1
            cur_end = end
            ret += 1

print(ret)
