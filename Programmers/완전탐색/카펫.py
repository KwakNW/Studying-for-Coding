def solution(brown, yellow):
    total = brown + yellow
    matrix = []
    for i in range(3, total // 2 + 1):
        if (total % i == 0) and (i-2)*(total//i - 2) == yellow:
            matrix.append((i, total // i))
    
    matrix.sort(reverse = True)
    return matrix[0]
