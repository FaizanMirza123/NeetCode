class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,n in enumerate(nums):
            diff=target-n # 7-3 =4, 7-4=3
            if diff in seen: # 3 is not in seen (VALUE not key) , now 3 in seen
                return [seen[diff],i] 
            seen[n]=i # now store 3 with index as key
1        