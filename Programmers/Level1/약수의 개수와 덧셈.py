def solution(left, right):
    # 약수의 개수 구해서 짝수이면 True 홀수이면 False 반환
    def divisor(num):
        cnt = 0
        for i in range(1, num+1):
            if num % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            return True
        else:
            return False
    answer = 0
    for i in range(left, right+1):
        if divisor(i):
            answer += i
        else:
            answer -= i
    return answer
