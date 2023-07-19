class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Utilize an unordered_map to store the val:index first
        unordered_map<int, int> index_val_map;

        // find (target - nums[i]) in the map, if exists,
        // return the result vecotr<int> {i, map[(target - nums[i])]}
        // else add the pair into the map
        for (int i=0; i<nums.size(); i++){
            if(index_val_map.find(target - nums[i]) != index_val_map.end()){
                return vector<int> {i, index_val_map[target - nums[i]]};
            }
            else{
                index_val_map.insert(pair<int, int>{nums[i], i});
            }
        }
        return vector<int> {0, 0};
    }
};