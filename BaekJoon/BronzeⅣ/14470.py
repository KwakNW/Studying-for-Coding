import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())

time = 0
if A < 0:
    time += abs(A) * C
    time += D
    time += B*E
elif A == 0:
    time += D
    time += B*E
else:
    time += (B-A)*E

print(time)
