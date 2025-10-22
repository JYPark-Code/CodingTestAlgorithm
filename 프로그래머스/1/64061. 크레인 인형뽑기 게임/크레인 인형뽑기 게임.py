def solution(board, moves):
    # 우리가 원하는 move를 활용할 수 있는 stack 형태로 바꾸자
    N = len(board)
    stack_board = [[] for _ in range(N)]
    answer = 0


    for i in range(N):
        for j in range(N-1, -1, -1):
            if board[j][i] == 0:
                continue
            stack_board[i].append(board[j][i])

    # print(stack_board) # [[3, 4, 0, 0, 0], [5, 2, 2, 0, 0], [1, 4, 5, 1, 0], [3, 4, 0, 0, 0], [1, 2, 1, 3, 0]]
    # 0 소거 하면 [[3, 4], [5, 2, 2], [1, 4, 5, 1], [3, 4], [1, 2, 1, 3]]

    storage = []

    for move in moves:
        # 비어있는 곳이면 넘어감
        if len(stack_board[move-1]) == 0:
            continue

        storage.append(stack_board[move-1].pop())

        if len(storage) < 2:
            continue
        else:
            if storage[-2] == storage[-1]:
                storage = storage[:-2]
                answer += 2


    return answer