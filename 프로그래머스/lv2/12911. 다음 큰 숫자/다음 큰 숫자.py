def solution(n):
    
    n_bin = str(bin(n)[2:])
    count_one = n_bin.count('1')
    
    new_num = n + 1
    
    while True:
        
        if str(bin(new_num)[2:]).count('1') == count_one:
            return int(new_num)
        
        else:
            new_num += 1