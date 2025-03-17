import math
def solution(fees, records):
    
    entry_time = {}
    fee_dict = {}
    
    for record in records:
        time, bus_num, status = record.split()
        
        if status == "IN":
            entry_time[bus_num] = time_to_minutes(time)
            
        elif status == "OUT":
            in_time = entry_time.pop(bus_num)
            stayed_time = time_to_minutes(time) - in_time
            fee_dict[bus_num] = fee_dict.get(bus_num, 0) + stayed_time
    
    for bus_num, in_time in entry_time.items():
        stayed_time = time_to_minutes("23:59") - in_time
        fee_dict[bus_num] = fee_dict.get(bus_num, 0) + stayed_time
    
    # 차량 번호 기준 정렬 후 요금 계산
    return [calculate_fee(fees, time) for car, time in sorted(fee_dict.items())]

# 출차된 기록이 없으면 23:59분에 출차되었다고 간주한다.
# 차량 번호가 작은 자동차부터 순서대로

def calculate_fee(fees, time):
    base_time, base_fee, extra_time, extra_fee = fees
    
    if time <= base_time:
        return base_fee
    
    else:
        return base_fee +  math.ceil((time - base_time) / extra_time) * extra_fee 
    
    


def time_to_minutes(time_str):
    hh, mm = map(int, time_str.split(":"))
    return hh * 60 + mm