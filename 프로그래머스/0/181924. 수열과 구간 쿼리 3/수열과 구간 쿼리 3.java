class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        
        for(int[] query : queries){
            int a = query[0];
            int b = query[1];
            
            swap(arr, a, b);
        }
        
        // int[] answer = {};
        return arr;
    }
    
    void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
}