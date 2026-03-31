class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,unordered_map<char,int>> test(strs.size());
        vector<vector<string>> result;
        unordered_map<string,bool> picked;

        for (auto& str : strs){
            unordered_map<char,int> ana;
            for (auto& c : str){
                ana[c] += 1;
            }
            test[str] = ana;
            picked[str] = false;
        }

        for (int i = 0 ; i < strs.size(); i++){
            cout<<picked[strs[i]]<<endl;
            vector<string> res;
            if (!picked[strs[i]]) {
                res.push_back(strs[i]);
                picked[strs[i]] = true;
            }else{
                continue;
            }
            for(int j = i+1; j<strs.size(); j++){
                if(test[strs[i]] == test[strs[j]]){
                    res.push_back(strs[j]);
                    picked[strs[j]] = true;
                }
            }
            if(!res.empty()) result.push_back(res);
        }
        return result;
    }
};
