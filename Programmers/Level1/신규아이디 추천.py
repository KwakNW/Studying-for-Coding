def solution(new_id):
    answer = ''
    # 1단계 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계 가능문자만 남겨놓기
    for id in new_id:
        if id.isalpha() or id.isdigit() or id in ['-', '_', '.']:
            answer += id
            
    # 3단계 연속 마침표 지우기
    while '..' in answer:
        answer = answer.replace("..", ".")
        
    # 4단계 처음이나 끝에 마침표 없애기
    answer = answer.strip(".")
    
    # 5단계 빈 문자열이라면 "a" 대입하기
    if answer == "":
        answer += 'a'
        
    # 6단계 길이가 16개 이상이면 15개의 문자만을 남겨놓고 모두 제거
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.strip(".")
        
    # 7단계 길이가 2자 이하라면 마지막 문자열 반복해서 길이 3으로 만들기
    while len(answer) <= 2:
        answer += answer[-1]
    return answer
