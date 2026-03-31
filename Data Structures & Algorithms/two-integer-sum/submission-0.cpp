class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        for (int i=0; i < nums.size()-1; i++){
            int b = target - nums[i];
            for (int j=i+1;  j < nums.size();j++){
                if (b==nums[j]){
                    return(vector<int>{i,j});
                }
            }
        }
    }
};
