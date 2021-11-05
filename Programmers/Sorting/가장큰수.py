# 처음 푼 방식 -> 순열함수 이용 (시간 초과)
from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = list(map(''.join, permutations(numbers, len(numbers))))
    numbers.sort(reverse = True)

    return numbers[0]
  

# 다시 푼 방식 -> 1000이하이기 때문에 한자리수도 3자리로 맞춰주기 위해 x*3 반복
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True)
    answer = ''.join(numbers)
    return answer
