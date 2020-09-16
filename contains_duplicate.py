# a hashtable will run in O(n) here for time and space
# more efficient if size is unknown

# if the given arrays will never be very large 
# it could be more efficient to sort the array 
# then iterate through the array comparing two adjacent
# values if they are the same return true

class Solution:  
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        
        for n in nums:
            if n in hashtable:
                return True
            
            hashtable[n] = 1
        
        return False