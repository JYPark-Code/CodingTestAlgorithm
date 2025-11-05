class Solution {
    public int solution(int[][] board, int k) {
        int answer = 0;
        int il = board.length;
        int jl = board[0].length;
        
        System.out.println(il + " " + jl);
        
        for(int i = 0; i< il; i++){
            for(int j = 0; j < jl; j++){
                if((i + j) <= k) {
                    answer += board[i][j];
                }
            }
        }
        
        
        return answer;
    }
}