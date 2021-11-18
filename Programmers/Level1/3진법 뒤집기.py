def solution(n):
    # 앞뒤 반전 3진수
    result = []
    while n != 0:
        result.append(n % 3)
        n //= 3
    
    answer = ''
    for r in result:
        answer += str(r)
        
    # 3진수 -> 10진수 변환
    answer = int(answer, 3)
    return answer
