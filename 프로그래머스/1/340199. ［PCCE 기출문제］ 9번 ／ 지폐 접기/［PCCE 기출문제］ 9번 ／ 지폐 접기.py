def solution(wallet, bill):
    answer = 0
    
    while True:
        
        if max(wallet) >= max(bill) and min(wallet) >= min(bill):
            break
        
        wrapBill(bill)
        
        answer += 1
    
    
    return answer


def wrapBill(bill):
    if bill[0] >= bill[1]:
        bill[0] //= 2
    else:
        bill[1] //= 2
    return bill