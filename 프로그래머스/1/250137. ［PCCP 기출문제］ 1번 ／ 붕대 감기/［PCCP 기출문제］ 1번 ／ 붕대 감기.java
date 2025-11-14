class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        // bandage [시전 시간, 초당 회복량, 추가 회복량]
        // attacks[i]는 [공격 시간, 피해량] 
        // 공격이 끝나고 남은 체력 return
        // 0 이하 죽으면 -1 return
        
        // boolean can_heal = true;
        
        int last_attack = attacks.length - 1;
        int end = attacks[last_attack][0];
        int current_health = health;
        
        for (int i = 0; i < last_attack; i++){
            
            // System.out.println(i + "번 공격 예정, " + "현재 체력 : " + current_health);
            
            int gap_time = attacks[i+1][0] - attacks[i][0];
            
            // System.out.println("다음 공격까지 : " + gap_time);
            
            // 즉사
            if ( (current_health - attacks[i][1]) <= 0){
                return -1;
            }
            
            if (gap_time > 1){
                
//                 System.out.println("현재 체력 : " + current_health + " - 현재 공격 : " + attacks[i][1] + " + 힐 예정량 : " + heal(bandage, gap_time));
                
                current_health = current_health - attacks[i][1] + 
                heal(bandage, gap_time);
                }
            
            
            else{
                // System.out.println("현재 체력 : " + current_health + " - 현재 공격 : " + attacks[i][1]);
                current_health -= attacks[i][1];
                }
            
            // System.out.println(i + "번째 공격, 현재 체력: " + current_health + " 입은 데미지 : " + attacks[i][1]);
            
            if (current_health <= 0)
                return -1;
                
            if (current_health >= health)
                current_health = health;
            
        }
        
        current_health -= attacks[last_attack][1];
        
        // System.out.println("마지막 공격, 현재 체력 : " + current_health + " 입은 데미지 : " + attacks[last_attack][1]);
        
        if (current_health <= 0)
            return -1;
        
        return current_health;
            
            
    }
    
    public int heal(int[] bandage, int time) {
        int process_time = bandage[0];
        int heal_amount = bandage[1];
        int bonus_heal = bandage[2];
        int healSecond = time - 1;

        if (healSecond <= 0){
            return 0;
        }

        int total = heal_amount * healSecond;

        int fullCasts = healSecond / process_time;

        total += fullCasts * bonus_heal;

        return total;
    }
}