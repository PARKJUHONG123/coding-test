import sys

def get_minimal(n):
    length = len(str(n))
    target = '1' * length

    if int(target) < n:
        target += '1'
        length += 1

    while True:
        int_target = int(target)
        if int_target % n == 0:
            return length

        target += '1'
        length += 1

def get_answer():
    input_value = sys.stdin.readline()
    if input_value is None or input_value == '':
        return -1
    elif int(input_value) % 2 == 0 or int(input_value) % 5 == 0:
        return -1
    else:
        return get_minimal(int(input_value))

while True:
    ret = get_answer()
    if ret == -1:
        break
    else:
        print(ret)