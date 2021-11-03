import sys

N = int(sys.stdin.readline())

if N != 0:
    P = list(map(int, sys.stdin.readline().split()))
    try:
        print("%0.2f" %((sum(P) / N) / (sum(P) / N)))
    except:
        print("divide by zero")
else:
    print("divide by zero")
