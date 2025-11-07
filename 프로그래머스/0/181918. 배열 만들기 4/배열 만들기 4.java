import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr) {
        List<Integer> stk = new ArrayList<>();
        for (int x : arr) {
            while (!stk.isEmpty() && stk.get(stk.size() - 1) >= x) {
                stk.remove(stk.size() - 1);   // pop
            }
            stk.add(x); // 비었거나 top < x 일 때 push
        }
        return stk;
    }
}