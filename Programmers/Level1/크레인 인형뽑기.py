def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                # 이전에 넣은 값과 동일하면 제거하고 제거 인형 수(answer) 증가
                if len(stack) != 0 and stack[-1] == board[i][m-1]:
                    board[i][m-1] = 0
                    stack = stack[:-1]
                    answer += 2
                    break
                else:
                    stack.append(board[i][m-1])
                    board[i][m-1] = 0
                    break
                
    return answer
