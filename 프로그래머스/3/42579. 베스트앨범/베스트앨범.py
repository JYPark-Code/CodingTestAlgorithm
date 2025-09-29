def solution(genres, plays):
    
    # 장르별로 곡과 재생 수를 담을 딕셔너리 생성
    album = {}

    # genres와 plays를 순회하며 album 딕셔너리 구성
    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in album:
            album[genre] = []  # 해당 장르가 딕셔너리에 없을 경우 리스트로 초기화
        album[genre].append((play, index))  # 재생 수와 인덱스를 해당 장르 리스트에 추가
        
    # print(album)
    # print(album.items())
    # 장르별 총 재생 수를 계산하여 정렬
    genre_play_count = {genre: sum(play for play, _ in plays) for genre, plays in album.items()}
    # print(genre_play_count)
    sorted_genres = sorted(genre_play_count.keys(), key=lambda x: genre_play_count[x], reverse=True)
    # print(sorted_genres)
    
    # 정답을 담을 리스트
    result = []

    # 정렬된 장르 순서대로 2곡씩 추출
    for genre in sorted_genres:
        # 해당 장르에서 재생 수가 많은 순으로 정렬 (재생 수가 같다면 인덱스 순으로 정렬)
        top_songs = sorted(album[genre], key=lambda x: (-x[0], x[1]))
        # print(top_songs)
        
        # 최대 두 곡의 인덱스를 result에 추가
        result.extend([index for _, index in top_songs[:2]])

    return result