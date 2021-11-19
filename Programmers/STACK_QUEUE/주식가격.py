from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices):
        price = prices.popleft()
        cnt = 0
        for p in prices:
            if price > p:
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt)
    return answer
