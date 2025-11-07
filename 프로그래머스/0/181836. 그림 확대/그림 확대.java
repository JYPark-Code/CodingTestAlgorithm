import java.util.*;

class Solution {
    public List<String> solution(String[] picture, int k) {
        List<String> answer = new ArrayList<>();
        
        for(String s : picture){
            String nTimes = "";
            for(int i = 0; i < s.length(); i++){
                char ch = s.charAt(i);
                nTimes += String.valueOf(ch).repeat(k);   
            }
            answer.addAll(Collections.nCopies(k, nTimes));
        }
        
        
        return answer;
    }
}