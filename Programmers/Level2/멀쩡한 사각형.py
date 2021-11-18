def solution(w,h):
    # 최대공약수 구하기 (유클리드 호제법)
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    GCD = gcd(min(w, h), max(w, h))
    return w*h - (w//GCD + h//GCD - 1) * GCD
            
