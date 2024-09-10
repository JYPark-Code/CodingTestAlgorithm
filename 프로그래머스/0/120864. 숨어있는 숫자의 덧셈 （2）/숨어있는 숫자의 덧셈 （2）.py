def solution(my_string):
    
    # isalpha(), isdecimal()
    num_list = []
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, " ")
    
    my_string = [ int(x) for x in my_string.strip().split(" ") if x != '']

    return sum(my_string)