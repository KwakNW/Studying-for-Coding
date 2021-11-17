def dfs(n, computers, start, visited):
    visited[start] = True
    for i in range(n):
        if visited[i] == False and computers[start][i] == 1: # 방문하지 않았을 때, 그리고 연결돼있을 때
            dfs(n, computers, i, visited)

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer += 1
    return answer
