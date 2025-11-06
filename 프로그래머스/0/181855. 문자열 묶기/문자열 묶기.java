import java.util.*;
class Solution {
    public int solution(String[] strArr) {
        int answer = 0;
        
        Map<Integer,List<String>> dict = new HashMap<>();
        for (String s : strArr){
            dict.computeIfAbsent(s.length(), k -> new ArrayList<>()).add(s);
        }
        
        // System.out.println(dict);
        
        for (List<String> list : dict.values()){
            if (list.size() > answer){
                answer = list.size();
            }
        }
        
        return answer;
    }
}