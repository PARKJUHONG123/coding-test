import sys

N = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))

def get_min(window, target_value):
    min_index, min_value = -1, sys.maxsize
    for index, value in enumerate(window):
        if value > target_value and min_value > value:
            min_value = value
            min_index = index
    return min_index, min_value

def next_value():
    if N == 1:
        return -1    
    start_index = -2

    while start_index >= -N:
        slide_window = num_list[start_index : ]
        if sorted(slide_window, reverse=True) == slide_window:        
            start_index -= 1
        else:
            target_value = slide_window[0]
            left_window = slide_window[1:]
            min_index, min_value = get_min(left_window, target_value)
            left_window[min_index] = target_value
            
            return ' '.join(map(str, num_list[:start_index] + [min_value] + sorted(left_window)))

    return -1

print(next_value())