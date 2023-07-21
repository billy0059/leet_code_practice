class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Create a set by the vector
        unordered_set<int> nums_set(nums.begin(), nums.end());
        int ret_size = 0;
        for (const auto& num: nums_set){
            if (nums_set.find(num-1) == nums_set.end()){ //num can be the first of the sequence
                int seq = num;
                int len = 0;
                while (nums_set.find(seq) != nums_set.end()){
                    len++;
                    seq++;
                }
                ret_size = len > ret_size ? len: ret_size;
            }
        }
        return ret_size;
    }
};