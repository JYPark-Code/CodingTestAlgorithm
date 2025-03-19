def solution(routes):
    
    # 출구 오름차순으로 정리
    routes.sort(key= lambda x: x[1])
    print(routes)
    
    camera = []
    i = 0
    
    for idx, route in enumerate(routes):
        entry, exit = route 
        if idx == 0:
            camera.append(exit)
        
        if camera[i] in range(entry, exit+1):
            continue
        
        else:
            camera.append(exit)
            i += 1
        
        # print("camera : ", camera)
        
    return len(camera)