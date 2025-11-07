import java.util.*;

class Solution {
    public int solution(int[] arr) {
        int [] before = arr.clone();
        // System.out.println(Arrays.toString(before));
        int answer = 0;
        
        while(true) {
            
            
            for(int i = 0; i < arr.length; i++){
                if(arr[i] >= 50 && arr[i] % 2 == 0){
                    arr[i] /= 2;
                } else if (arr[i]< 50 && arr[i] % 2 == 1){
                    arr[i] = arr[i] * 2 + 1;
                }
            }
                
            if(Arrays.equals(arr, before)){
                break; 
            }
            
            before = arr.clone();
            answer += 1; // count
            
        }  
        return answer;
    }
}