class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> ele;
        for (int i = 0 ; i < nums.size(); i ++){
            auto it = ele.find(nums[i]);
            if(it != ele.end()){
                return true;
            }else{
                ele.insert(nums[i]);
            }
        }

        return false;
    }
};