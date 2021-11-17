def solution(lottos, win_nums):
    answer = []
    result = 0
    for i in range(6):
        if lottos[i] in win_nums:
            result += 1
    zero = lottos.count(0)
    
    if 7 - (result + zero) > 5:
        answer.append(6)
    else:
        answer.append(7 - (result + zero))
    
    if 7 - result > 5:
        answer.append(6)
    else:
        answer.append(7 - result)
    return answer
