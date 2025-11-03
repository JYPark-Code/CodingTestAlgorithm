import java.util.*;
class Solution {
    public int solution(int[] num_list, int n) {
        
        if(Arrays.stream(num_list).anyMatch(i -> i == n)){
            return 1;
        }
        return 0;
    }
}