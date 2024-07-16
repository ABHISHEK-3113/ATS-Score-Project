class Solution {
public:
    int maxArea(vector<int>& height) { 

        int n = height.size(); 
        int ans =0; 
        int l = 0; 
        int r = n-1;  

        while (l < r){
   
            int s = min(height[l],(int) height[r]); 

            int area = (r-l) * s; 

            ans = max(area, ans);

            if (height[l] < height[r]){
                l++;
            }
            else{
                r--; 
            }

        }
        

        return ans; 
    }
};
