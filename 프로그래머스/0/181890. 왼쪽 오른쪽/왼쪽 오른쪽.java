import java.util.*;
    
class Solution {
    public List<String> solution(String[] str_list) {
        int n = str_list.length;
        int idxL = -1, idxR = -1;

        // 첫 등장 위치 찾기
        for (int i = 0; i < n; i++) {
            if (idxL == -1 && "l".equals(str_list[i])) idxL = i;
            if (idxR == -1 && "r".equals(str_list[i])) idxR = i;
            if (idxL != -1 && idxR != -1) break;
        }

        // 둘 다 없는 경우
        if (idxL == -1 && idxR == -1) return new ArrayList<>();

        // 첫 등장이 l이 먼저거나 r이 없으면: 왼쪽 조각 [0, idxL)
        if (idxR == -1 || (idxL != -1 && idxL < idxR)) {
            return new ArrayList<>(Arrays.asList(str_list).subList(0, idxL));
        }

        // 첫 등장이 r이 먼저거나 l이 없으면: 오른쪽 조각 (idxR, n)
        return new ArrayList<>(Arrays.asList(str_list).subList(idxR + 1, n));
    }
}