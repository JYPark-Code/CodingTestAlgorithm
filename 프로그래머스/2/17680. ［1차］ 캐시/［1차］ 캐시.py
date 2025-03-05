def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    answer = 0
    
    cache_mem = []
    
    for city in cities:
        city = city.lower()
        
        if city in cache_mem:
            answer += 1
            cache_mem.remove(city)
        
        else:
            answer += 5
            if len(cache_mem) >= cacheSize:
                cache_mem.pop(0)
        
        cache_mem.append(city)
    
    return answer