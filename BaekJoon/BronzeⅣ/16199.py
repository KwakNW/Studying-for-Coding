import sys

Y, M, D = map(int, sys.stdin.readline().split())
YEAR, MONTH, DAY = map(int, sys.stdin.readline().split())

# 만 나이
if MONTH > M:
    print(YEAR - Y)
elif MONTH == M:
    if DAY >= D:
        print(YEAR - Y)
    else:
        print(YEAR - Y - 1)
else:
    print(YEAR - Y - 1)

# 세는 나이
print(YEAR - Y + 1)

# 연 나이
print(YEAR - Y)
