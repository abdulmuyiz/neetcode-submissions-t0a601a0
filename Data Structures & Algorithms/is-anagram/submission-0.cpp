class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> characters;
        if (s.size() != t.size()) return false;
        for (int i ; i < s.size(); i++){
            characters[s[i]] += 1;
        }

        for (int i ; i < s.size(); i++){
            characters[t[i]] -= 1;
            if(characters[t[i]]<0) return false;
        }

        return true;
    }
};
