def solution(answers):
    Num = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    result = [0]*3
    for i in range(3):
        for j in range(len(answers)):
            if Num[i][j%len(Num[i])] == answers[j]:
                result[i] += 1
    
    answer = []
    for i in range(3):
        if result[i] == max(result):
            answer.append(i+1)
            
    return answer
