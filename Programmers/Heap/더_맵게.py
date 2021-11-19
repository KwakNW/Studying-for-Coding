import heapq

def solution(scoville, K):
    # heapq를 이용하여 정렬수행
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    
    cnt = 0
    while heap[0] < K:
        try:
            new = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
            heapq.heappush(heap, new)
        except:
            return -1
        cnt += 1
    return cnt
