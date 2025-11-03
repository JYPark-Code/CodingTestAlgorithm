class Solution {
    public int solution(int a, int b) {
        String sa = String.valueOf(a);
        String sb = String.valueOf(b);
        int la = sa.length();
        int lb = sb.length();
        int total_length = la + lb;
            
        // System.out.println(la + " " + lb);
        
        int ab = (a *  (int) Math.pow(10, lb)) + b;
        int ba = (b *  (int) Math.pow(10 ,la)) + a;
        
        if (ab > ba){
            return ab;
        } else {
            return ba;
        }
        
    }
}