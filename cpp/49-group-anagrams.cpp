class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;

        // Utilize sorted string for the anagram id
        for(const auto& str: strs){
            string anagram_id = str;
            sort(anagram_id.begin(), anagram_id.end());
            map[anagram_id].push_back(str);
        }

        vector<vector<string>> ret_vec;
        for(const auto& m: map){
            ret_vec.push_back(m.second);
        }
        return ret_vec;
    }
};