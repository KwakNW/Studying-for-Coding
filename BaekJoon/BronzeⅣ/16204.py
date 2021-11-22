import sys

N, M, K = map(int, sys.stdin.readline().split())

answer = min(M, K)
answer += min(N-M, N-K)

print(answer)
