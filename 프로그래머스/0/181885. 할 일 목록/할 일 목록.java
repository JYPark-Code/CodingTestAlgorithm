import java.util.ArrayList;

class Solution {
    public  ArrayList<String> solution(String[] todo_list, boolean[] finished) {
        ArrayList<String> answer = new ArrayList<>();
        
        int size = todo_list.length;
        
        for (int i = 0; i < size; i++){
            if (finished[i] == false){
                    answer.add(todo_list[i]);
            }
        } 
        
        return answer;
    }
}