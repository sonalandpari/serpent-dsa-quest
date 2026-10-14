class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        i=0
        j=len(nums)-1
        sum=nums[i]+nums[j]
        while sum!=target:
            sum=nums[i]+nums[j]
            if sum<target:
                i+=1
            elif sum>target:
                j-=1
            
        return i,j

print(Solution().twoSum([2,7,11,15], 9))