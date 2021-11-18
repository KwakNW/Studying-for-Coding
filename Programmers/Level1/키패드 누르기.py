def solution(numbers, hand):
    answer = ''
    l_hand = 10
    r_hand = 12
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            l_hand = num
        elif num in [3, 6, 9]:
            answer += "R"
            r_hand = num
        else:
            if num == 0:
                num = 11
                
            # 거리 측정
            l_dis = (abs(num - l_hand) // 3) + (abs(num - l_hand) % 3)
            r_dis = (abs(num - r_hand) // 3) + (abs(num - r_hand) % 3)
            
            if l_dis < r_dis:
                answer += "L"
                l_hand = num
            elif l_dis > r_dis:
                answer+= "R"
                r_hand = num
            else:
                if hand == "right":
                    answer += "R"
                    r_hand = num
                else:
                    answer += "L"
                    l_hand = num
            
    return answer
