def solution(number, limit, power):
    
    answer = 0
    
    for i in range(1, number + 1):
        
        if getDivLength(i) <= limit:
            answer += getDivLength(i)
        else:
            answer += power
    
    return answer


def getDivLength(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return len(divisorsList)