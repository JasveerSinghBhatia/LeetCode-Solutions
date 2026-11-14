class Solution {
public:
    bool fun(unordered_map<char,int> &have, unordered_map<char,int> &need){
        for(auto i:need){
            char ch = i.first;
            int fneed = i.second;
            int fhave = have[ch];

            if(fhave<fneed) return false;
        }
        return true;
    }
    bool canConstruct(string ransomNote, string magazine) {
        int n=ransomNote.length();
        int m=magazine.length();
        unordered_map<char,int> need;
        unordered_map<char,int> have;

        for(int i=0;i<n;i++){
            need[ransomNote[i]]++;
        }
        for(int i=0;i<m;i++){
            have[magazine[i]]++;
        }
        return fun(have,need);
    }
};