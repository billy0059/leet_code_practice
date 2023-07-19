class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // Using unordered_set for the find time: complexity O(1)
        std::unordered_set<int> check;
        for (const auto&n: nums){
            if (check.find(n) != check.end()){ // the number is in the set
                return true;
            }
            else{
                check.insert(n);
            }
        }
        return false;
    }
};