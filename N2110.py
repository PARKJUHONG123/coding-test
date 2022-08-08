import sys
arr = list()
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()
left_distance = 1
right_distance = arr[-1] - arr[0]

while left_distance <= right_distance:
    mid_distance = (left_distance + right_distance) // 2
    start_locate = arr[0]
    wifi_need = 1
    
    for index in range(1, n):
        compare_distance = arr[index] - start_locate
        if compare_distance >= mid_distance:
            wifi_need += 1
            start_locate = arr[index]
            
    if wifi_need >= m:
        left_distance = mid_distance + 1
    else:
        right_distance = mid_distance - 1

print(right_distance)