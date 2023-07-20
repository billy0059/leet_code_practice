class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // First create a vector, where vec[i] is the product of nums[0~i-1]
        vector<int> ret_vec(nums.size(), 1);
        for (int i=1; i<nums.size(); i++){
            ret_vec[i] = nums[i-1] * ret_vec[i-1];
        }

        // Then do the multiplication from the tail to the head, then we'll get the answer vector.
        int post_product = 1;
        for (int i=ret_vec.size()-1; i>=0; i--){
            ret_vec[i] *= post_product;
            post_product *= nums[i];
        }

        return ret_vec;
    }
};