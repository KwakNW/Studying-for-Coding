from itertools import combinations

def solution(nums):
    # 소수 판별 함수
    def is_prime(number):
        result = 0
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
    # 3개씩 더하기
    sum_list = []
    for comb in list(combinations(nums, 3)):
        sum_list.append(sum(comb))
        
    # 소수 판별
    answer = 0
    for s in sum_list:
        if is_prime(s):
            answer += 1
    return answer
