import sys

A, B, C = map(int, sys.stdin.readline().split())
print(int(max(A*B/C, A/B*C)))
