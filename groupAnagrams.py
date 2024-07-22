class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if strs is None:
            return [""] 
        
        mp = defaultdict(list) 

        for word in strs:
            sortedword = ''.join(sorted(word)) 
            mp[sortedword].append(word) 
        

        return list(mp.values()) 
        
