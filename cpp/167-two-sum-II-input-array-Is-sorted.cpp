class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> ret_indices;
        int l=0, r=numbers.size()-1;
        while (l<r){
            if(numbers[l]+numbers[r] == target){
                ret_indices.push_back(l+1);
                ret_indices.push_back(r+1);
                return ret_indices;
            }
            else if (numbers[l]+numbers[r] > target){
                r--;
            }
            else{
                l++;
            }
        }
        return ret_indices;
    }
};