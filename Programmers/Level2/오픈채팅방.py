def solution(record):
    # 명령어와 아이디 담는 리스트
    _id = []
    
    # id와 별명 담는 사전
    _name = {}
    
    for r in record:
        r = r.split()
        _id.append([r[0], r[1]])
        
        if r[0] in ['Enter', 'Change']:
            _name[r[1]] = r[2]
    
    answer = []
    for i in _id:
        COMM, ID = i
        if COMM == "Enter":
            answer.append(_name[ID] + "님이 들어왔습니다.")
        elif COMM == "Leave":
            answer.append(_name[ID] + "님이 나갔습니다.")
    return answer
