class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }
        // init the check map, with all char value = 0
        unordered_map<char, int> anagram_check_map;
        for (int i=0; i<26; i++){
            anagram_check_map.insert(pair<char, int>('a'+i, 0));
        }

        for (const auto& c : s){
            anagram_check_map[c] += 1;
        }
        for (const auto& c : t){
            anagram_check_map[c] -= 1;
        }
        for (const auto& map : anagram_check_map){
            if (map.second != 0){
                return false;
            }
        }
        return true;
    }
};