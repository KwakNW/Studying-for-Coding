import sys

A, B = map(int, sys.stdin.readline().split())

q = A // B
r = A % B

if r < 0:
    q += 1
    r += abs(B)

print(q)
print(r)
