def solution(clothes):
    dict = {}
    for v, k in clothes:
        if k in dict:
            dict[k] += 1
        else:
            dict[k] = 1
    
    cloth = [x + 1 for x in list(dict.values())] # 해당 옷을 안입는 경우 1개를 추가해주기
    answer = 1
    for c in cloth:
        answer *= c
        
    return answer - 1
