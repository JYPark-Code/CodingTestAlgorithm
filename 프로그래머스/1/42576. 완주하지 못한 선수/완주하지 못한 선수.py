# def solution(participant, completion):
    
#     p_count_list = list()
#     c_count_list = list()
    
#     for p in participant:
#         p_count_list.append(participant.count(p))
    
#     for p in completion:
#         c_count_list.append(completion.count(p))
    
#     participant_dict = dict(zip(participant,p_count_list))
#     completion_dict = dict(zip(completion,c_count_list))
    
#     res = {key: participant_dict[key] - completion_dict.get(key, 0)
#             for key in participant_dict.keys()}
    
#     for key, value in res.items():
#         if value == 1:
#             return key

def solution(participant, completion):
    participant_dict = {}
    
    for person in participant:
        if person in participant_dict:
            participant_dict[person] += 1
        else:
            participant_dict[person] = 1

    for person in completion:
        if person in participant_dict:
            participant_dict[person] -= 1
            if participant_dict[person] == 0:
                del participant_dict[person]

    return list(participant_dict.keys())[0]
    
        
    
        
