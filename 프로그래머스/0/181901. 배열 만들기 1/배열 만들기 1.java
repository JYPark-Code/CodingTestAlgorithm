import java.util.*;

class Solution {
    public List<Integer> solution(int n, int k) {
        List<Integer> answer = new ArrayList<>();
        int cur = k;
        while(cur <= n){
            answer.add(cur);
            cur += k;
        }
        
        return answer;
    }
}