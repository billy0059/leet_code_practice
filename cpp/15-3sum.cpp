class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector< vector<int> > ret_vec;
        // Sort the given nums vector first, and each -(nums[i]) would be the "target" for nums[i+1~]
        sort(nums.begin(), nums.end());
        int i=0;
        while (i < nums.size()-2){
            if(i>0){
                while(nums[i]==nums[i-1] && i<nums.size()-2) i++; //Skip the same target.
            }
            int target = -nums[i]; // Now the problem changes to "two sum II"
            int l=i+1, r=nums.size()-1;
            while(l<r){
                if((nums[l] + nums[r]) > target){
                    r--;
                }
                else if ((nums[l] + nums[r]) < target){
                    l++;
                }
                else{ // Valid, add the result
                    ret_vec.push_back(vector<int>{nums[i], nums[r], nums[l]});
                    l++;
                    while(nums[l] == nums[l-1] && l<r){ // Skip the same value.
                        l++;
                    }
                }
            }
            i++;
        }
        return ret_vec;
    }
};