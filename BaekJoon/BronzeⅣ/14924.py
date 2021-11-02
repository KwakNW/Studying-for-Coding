import sys

S, T, D = map(int, sys.stdin.readline().split())

time = D/(S*2)
print(int(time * T))
