import java.util.*;

class Solution {
    public List<Integer> solution(String myString) {
        List<String> str_list = new ArrayList<>(Arrays.asList(myString.split("x", -1)));
        List<Integer> answer = new ArrayList<>();
        System.out.println(str_list);
        
        for(String s : str_list){
            answer.add(s.length());
        }
        
        return answer;
    }
}