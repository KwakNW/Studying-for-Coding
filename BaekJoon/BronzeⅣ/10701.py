import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
P = int(sys.stdin.readline())

if P > C:
    print(min(A*P, B + (P-C)*D))
else:
    print(min(A*P, B))
