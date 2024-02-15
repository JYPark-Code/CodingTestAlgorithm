def solution(phone_book):
    
    phone_book.sort()
    # print(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        
        # print("p1", p1)
        # print("p2", p2)
        
        if p2.startswith(p1):
            return False
        
    return True

    