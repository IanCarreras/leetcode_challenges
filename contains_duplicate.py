class Solution:  
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        
        for n in nums:
            if n in hashtable:
                return True
            
            hashtable[n] = 1
        
        return False