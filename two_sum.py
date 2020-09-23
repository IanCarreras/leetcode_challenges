class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        i = 0
        
        for n in nums:
            result = target - n
            
            if result in hashtable:
                return [i, hashtable[result]]
            
            if n not in hashtable:
                hashtable[n] = i
                
            i += 1