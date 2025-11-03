class Solution {
    public int solution(String myString, String pat) {
        String myString2 = "";
        for(char c : myString.toCharArray()){
            if (c == 'A'){
                myString2 += "B";
            } else if(c == 'B'){
                myString2 += "A";
            }   
        }
        
        if(myString2.contains(pat)){
            return 1;
        }
        return 0;
    }
}