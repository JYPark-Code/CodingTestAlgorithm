import java.util.*;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        
        if (arr1.length > arr2.length) {
            return 1;
        } else if (arr1.length < arr2.length) {
            return -1;
        } else if (arr1.length == arr2.length) {
            int one_sum = Arrays.stream(arr1).sum();
            int two_sum = Arrays.stream(arr2).sum();
            
            if (one_sum > two_sum) {
                return 1;
            } else if (one_sum == two_sum) {
                return 0;
            } else {
                return -1;
            }
        }
        return 0;
    }
}