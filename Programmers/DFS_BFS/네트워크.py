def dfs(n, computers, start, visited):
    visited[start] = True
    for i in range(n):
        if visited[i] == False and computers[start][i] == 1:
            dfs(n, computers, i, visited)
    return

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer += 1
    return answer
