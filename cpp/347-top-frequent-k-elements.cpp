class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Create a map, which the key is the number, the value is the occur times of the key.
        unordered_map<int, int> num_occur_map;
        for(const auto& num: nums){
            num_occur_map[num]++;
        }

        // Create a vector of vectors, which the index i is the occur time, vec[i] is the numbers that occur i times.
        std::vector<vector<int>> occur_num_vec(nums.size()+1, std::vector<int>{}); //size needs +1 since it is 0-index.
        for(const auto& map: num_occur_map){
            occur_num_vec[map.second].emplace_back(map.first);
        }


        // Create a ret vector for the top k frequent elements
        std::vector<int> ret_vec;

        int i = occur_num_vec.size()-1;
        while (k>0){
            if (occur_num_vec[i].size() != 0){
                k -= occur_num_vec[i].size();
                for (const auto& num: occur_num_vec[i]){
                    ret_vec.emplace_back(num);
                }
            }
            i--;
        }
        return ret_vec;
    }
};