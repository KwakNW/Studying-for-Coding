from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0 # 시간
    bridge_weight = 0 # 다리 위 트럭 무게
    on_bridge = deque([0 for _ in range(bridge_length)]) # 다리 위에 있는 트럭
    truck_weights = deque(truck_weights) # 대기 중인 트럭 무게
    
    while len(truck_weights) > 0 or bridge_weight > 0:
        truck = on_bridge.popleft() # 다리 통과
        bridge_weight -= truck
        
        # 새 트럭이 다리에 올라갈 수 있으면
        if len(truck_weights) > 0 and bridge_weight + truck_weights[0] <= weight: 
            newTruck = truck_weights.popleft()
            bridge_weight += newTruck
            on_bridge.append(newTruck) # 대기 트럭에서 하나 빼서 다리에 올림
            
        # 새 트럭이 다리에 올라갈 수 없으면
        else: 
            on_bridge.append(0) # 오른쪽에 0을 삽입해서 다리 길이 유지
        
        time += 1
    return time
