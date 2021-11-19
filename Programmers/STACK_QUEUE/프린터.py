from collections import deque

def solution(priorities, location):
    answer = 0
    # (값, 인덱스)로 deque 생성
    queue = deque([(value, index) for index, value in enumerate(priorities)])
    
    while len(queue) > 0:
        q = queue.popleft()
        if len(queue) == 0 or q[0] >= max(queue)[0]:
            answer += 1
            if q[1] == location:
                return answer
        else:
            queue.append(q)
