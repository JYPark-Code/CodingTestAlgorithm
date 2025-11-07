import java.util.*;

class Solution {
    public int[][] solution(int[][] arr) {
        int x = arr.length;
        int y = arr[0].length;
        int n = Math.max(x,y);
        
        if (x == y) return arr;
        
        int[][] answer = new int[n][n];
        
        for(int i = 0; i < x; i++){
            System.arraycopy(arr[i], 0, answer[i], 0, y);
        }
               
        
        
        return answer;
    }
}