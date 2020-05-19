def solution(board, moves):
    answer = 0
    pick = []
    for move in moves:
        for x in range(len(board)):
            # 해당 위치에 인형이 있다면
            if board[x][move-1]:
                # 바구니에 인형이 있고 제일 위 인형과 같다면
                if pick and pick[-1] == board[x][move-1]:
                    pick.pop()
                    answer += 2
                # 바구니가 비어있거나 제일 위 인형과 같지 않다면
                else:
                    pick.append(board[x][move-1])
                board[x][move-1] = 0
                break
    return answer