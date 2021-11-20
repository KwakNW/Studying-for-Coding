# 내가 푼 것
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True
    
    
# startswith 이용
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
    

# 다른 사람의 풀이
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    # ZIP 함수를 통해 두 개씩 짝 맞추기 
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
    
