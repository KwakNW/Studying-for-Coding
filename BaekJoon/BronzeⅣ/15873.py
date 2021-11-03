import sys

Num = sys.stdin.readline().strip()

if len(Num) == 2:
    print(int(Num[0]) + int(Num[1]))
elif Num[0] == '1':
    print(int(Num[:2]) + int(Num[2:]))
else:
    print(int(Num[:1]) + int(Num[1:]))
