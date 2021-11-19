from collections import defaultdict

def solution(tickets):
    dic = defaultdict(list)
    for start, end in tickets:
        dic[start].append(end)
    
    def dfs():
        stack = ["ICN"]
        while stack:
            airport = stack[-1]
            # 공항에서 갈 수 있는 길이 비어있으면
            if not dic[airport]:
                visited.append(stack.pop())
            else:
                stack.append(dic[airport].pop(0))
    
    visited = []
    for k in dic.keys():
        dic[k].sort()
    dfs()

    return visited[::-1]
