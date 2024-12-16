class Solution {
    public int solution(int a, int b) {
        
        String plusCircleStr = String.valueOf(a) + String.valueOf(b);
        int plusCircleInt = Integer.parseInt(plusCircleStr);
        
        if (plusCircleInt >= 2 * a * b) {
            return plusCircleInt;
        } else {
            return 2 * a * b;
        }
        
    }
}