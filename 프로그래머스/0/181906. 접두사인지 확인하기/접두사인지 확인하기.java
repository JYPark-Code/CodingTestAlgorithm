class Solution {
    public int solution(String my_string, String is_prefix) {
        int sub_length = is_prefix.length();
        System.out.println(sub_length);
            
        if (sub_length > my_string.length()){
            return 0;
        }
        
        if (is_prefix.equals(my_string.substring(0, sub_length))) {
            return 1;
        } 
        
        return 0;
    }
}