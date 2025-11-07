import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        
        for(char ch : my_string.toCharArray()){
            if ('A' <= ch && ch <= 'Z'){
                answer[ch - 'A']++;
            } else if('a' <= ch && ch <= 'z') {
                answer[26 + (ch - 'a')]++;
            }
        }
        
        return answer;
    }
}