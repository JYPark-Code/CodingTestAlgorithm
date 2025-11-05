import java.util.*;

class Solution {
    public String[] solution(String myString) {
        return Arrays.stream(myString.split("x"))
                     .filter(s -> !s.isEmpty()) // 빈 문자열 제거
                     .sorted()                  // 사전순 정렬
                     .toArray(String[]::new);   // 배열로 반환
    }
}