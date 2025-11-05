import java.util.*;

class Solution {
    public List<String> solution(String[] strArr) {
        List<String> answer = new ArrayList<>();
        String temp = "";
        
        for(int i = 0; i < strArr.length; i++){
            if (i % 2 == 0) {
                temp = strArr[i].toLowerCase();
                answer.add(temp);
            } else {
                temp = strArr[i].toUpperCase();
                answer.add(temp);
            }
        } 
        return answer;
    }
}