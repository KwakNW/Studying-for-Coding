from itertools import permutations

# 소수 판별 함수
def is_prime(x):
    count = 0
    for i in range(2, x+1):
        if x % i == 0:
            count += 1
            if count >= 2:
                return False
    if count < 2 and x > 1:
        return True

# 조합을 통해서 구현
def solution(numbers):
    answer = []
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        P_list = list(map(''.join, permutations(numbers, i)))
        for p in P_list:
            if is_prime(int(p)):
                answer.append(int(p))
    answer = list(set(answer))

    return len(answer)
