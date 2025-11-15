class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        boolean isStart = true;
        
        for(char c : s.toCharArray()){
            
            if(isStart){
                if (Character.isLetter(c)){
                    sb.append(Character.toUpperCase(c));
                } else {
                    sb.append(c);
                }
            } else {
                if (Character.isLetter(c)){
                    sb.append(Character.toLowerCase(c));
                } else {
                    sb.append(c);
                }
            }
            
            isStart = ( c == ' ');
            
        } 
        
        return sb.toString();
    }
}