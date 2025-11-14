import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        Set<Integer> lostSet = new HashSet<>();
        Set<Integer> reserveSet = new HashSet<>();
        
        for (int i : reserve){
            reserveSet.add(i);
        }
        
        for (int j : lost){
            lostSet.add(j);
        }
        
        Set<Integer> intersection = new HashSet<>(lostSet);
        intersection.retainAll(reserveSet);
        
        for (int x : intersection) {
            lostSet.remove(x);
            reserveSet.remove(x);
        }
        
        
        // 2단계: 남은 lost 학생들에 대해 왼쪽/오른쪽 친구에게 빌리기
        for (int l : new HashSet<>(lostSet)) { // 순회용 복사본
            if (reserveSet.contains(l - 1)) {
                reserveSet.remove(l - 1);
                lostSet.remove(l);
            } else if (reserveSet.contains(l + 1)) {
                reserveSet.remove(l + 1);
                lostSet.remove(l);
            }
        }

        // 체육복 있는 학생 수 = 전체 - 아직도 못 빌린 학생 수
        return n - lostSet.size();
        
        
        
    }
}