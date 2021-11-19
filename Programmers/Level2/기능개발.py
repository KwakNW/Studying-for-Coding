from math import ceil

def solution(progresses, speeds):
    # 작업이 완료될 때까지 걸리는 시간
    answer = []
    for i in range(len(progresses)):
        answer.append(ceil((100 - progresses[i]) / speeds[i]))
    
    # 앞의 작업시간을 포함하여 배포하는데 소요되는 시간
    for i in range(len(answer) - 1):
        if answer[i] > answer[i+1]:
            answer[i+1] = answer[i]
            
    # 배포하는 날에 배포되는 기능 수(사전)
    dic = {}
    for i in range(len(answer)):
        if answer[i] not in dic.keys():
            dic[answer[i]] = 1
        else:
            dic[answer[i]] += 1
            
    # value만 리스트로 저장
    result = []
    for k, v in dic.items():
        result.append(v)
        
    return result
