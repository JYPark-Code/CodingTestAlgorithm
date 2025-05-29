class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;
  
        //N = MAX_NUM, W = 넓이, NUM = CHOICE NUM
        int []width_num = new int[w];
        for(int i=0; i<w;i++)
        {
            width_num[i]=n/w;
        }
        
        if(n/w%2!=0) //홀수일 경우 오른쪽 시작 
        {
            for(int i=w-1;i>w-1-n%w;i--)
            {
                width_num[i]+=1;
            }
        }
        
        else if(n/w%2==0) 
        {
            for(int i=0;i<n%w;i++)
            {
                width_num[i]+=1;
            }
        }
    
        if(num%w==0 && num/w%2==0){  
            
            answer = width_num[0]-num/w+1;
        }
        else if(num%w==0 && num/w%2!=0){ 
           
            answer = width_num[w-1]-num/w+1;
        }
        
        if(num/w%2==0 && num%w!=0){
            
            answer = width_num[num%w-1]-num/w;
        }
        else if(num/w%2!=0 && num%w!=0){
            answer = width_num[w-num%w]-num/w;
        }
        return answer; 
    }
}