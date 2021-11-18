def solution(nums):
    poketmon = len(nums) // 2
    kind = list(set(nums))
    
    if len(kind) >= poketmon:
        return poketmon
    else:
        return len(kind)
