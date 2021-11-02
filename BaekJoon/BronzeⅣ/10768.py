import sys

M = int(sys.stdin.readline())
D = int(sys.stdin.readline())

if M < 2 or (M == 2 and D < 18):
    print("Before")
elif M == 2 and D == 18:
    print("Special")
else:
    print("After")
