def solution(babbling):
    
    available = ["aya", "ye", "woo", "ma"]
    modified_babbling = []
    
    for content in babbling:
        modified_content = content
        for word in available:
            modified_content = modified_content.replace(word, " ")
        modified_babbling.append(modified_content)
        
    modified_babbling = [x.strip(" ") for x in modified_babbling] 
    print(modified_babbling)
    
    return modified_babbling.count('')