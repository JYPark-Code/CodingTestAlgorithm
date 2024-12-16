import java.util.ArrayList;

class Solution {
    public ArrayList<String> solution(String[] names) {
        int size = names.length;
        int products = size / 5;
        
        // System.out.println(products);
        
        ArrayList<String> answer = new ArrayList<>();
        
        for (int i = 0; i <= products; i++){
            if (i*5 < size){
                answer.add(names[i*5]);
            }
        }
        
        return answer;
    }
}