def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # 여분을 가져왔지만 체육복을 도난당한 경우
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)
    
    return n - len(_lost)
