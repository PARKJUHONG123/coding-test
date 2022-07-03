from ast import Return
import collections


def cover(route):
    min_x = min(route, key = lambda x : x[0])[0]
    min_y = min(route, key = lambda x : x[1])[1]
    max_x = max(route, key = lambda x : x[0])[0]
    max_y = max(route, key = lambda x : x[1])[1]

    ret = [[0 for _ in range(max_y - min_y + 1)] for _ in range(max_x - min_x + 1)]

    for element in route:
        ret[element[0] - min_x][element[1] - min_y] = 1
    
    return ret

def get_rotates(blocks):
    targets = cover(blocks[:])
    rotate_list = list()
    rotate_list.append(targets)
    
    for _ in range(3):
        height, width = len(targets), len(targets[0])
        temp = [[0 for _ in range(height)] for _ in range(width)]
        for i in range(height):
            for j in range(width):
                temp[j][height - i - 1] = targets[i][j]
        rotate_list.append(temp)
        targets = temp[:]
    
    return rotate_list

def solution(game_board, table):
    answer = 0
    length = len(game_board)    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    queue_empty = collections.deque()
    queue_block = collections.deque()

    empty_list = list()
    block_list = list()

    for i in range(length):
        for j in range(length):

            if game_board[i][j] == 0:
                game_board[i][j] = 2
                queue_empty.append([i, j])
                empty = [[i, j]]

                while queue_empty:
                    qi, qj = queue_empty.popleft()
                    
                    for di, dj in direction:
                        ni, nj = qi + di, qj + dj

                        if 0 <= ni < length and 0 <= nj < length:
                            if game_board[ni][nj] == 0:
                                game_board[ni][nj] = 2
                                queue_empty.append([ni, nj])
                                empty.append([ni, nj])
                empty_list.append(empty)

            if table[i][j] == 1:
                table[i][j] = 2
                queue_block.append([i, j])
                block = [[i, j]]

                while queue_block:
                    qi, qj = queue_block.popleft()

                    for di, dj in direction:
                        ni, nj = qi + di, qj + dj

                        if 0 <= ni < length and 0 <= nj < length:
                            if table[ni][nj] == 1:
                                table[ni][nj] = 2
                                queue_block.append([ni, nj])
                                block.append([ni, nj])
                block_list.append(block)



    used_list = [False for _ in range(len(block_list))]
    full_list = [False for _ in range(len(empty_list))]


    for empty_index, emptys in enumerate(empty_list):
        for block_index, blocks in enumerate(block_list):
            if len(emptys) == len(blocks) and not used_list[block_index] and not full_list[empty_index]:

                target_empty = cover(emptys)
                rotated = get_rotates(blocks)
                for rotate in rotated:
                    if target_empty == rotate:
                        used_list[block_index] = True
                        full_list[empty_index] = True
                        answer += len(emptys)
                        break
    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]] ,	[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])

