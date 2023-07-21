class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0, r=height.size()-1;
        int ret_max = 0;
        int tmp_area = 0, tmp_height = 0;

        while(l<r){
            tmp_height = height[l] < height[r] ? height[l]: height[r];
            tmp_area = tmp_height * (r-l);
            ret_max = tmp_area > ret_max ? tmp_area: ret_max;
            if (height[l] < height[r]){
                l++;
                while(l<r && (height[l]<=height[l-1])) l++; // Skip the shorter height
            }
            else{
                r--;
                while(l<r && (height[r]<=height[r+1])) r--; // Skip the shorter height
            }
        }
        return ret_max;
    }
};