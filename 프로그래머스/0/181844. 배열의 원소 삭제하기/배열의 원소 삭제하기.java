import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        int [] result = Arrays.stream(arr)
            .filter(a -> Arrays.stream(delete_list).noneMatch(d -> d == a))
            .toArray();
        
        return result;
        
    }
}