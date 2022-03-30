class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        j=0
        min=nums[0]
        profit=[]
        for i in range(1,len(nums)):
            if nums[i]<min:
                min=nums[i]

            else:

                if j<nums[i]-min:
                    j=nums[i]-min
                    profit.append(j)
        if len(profit)>0:
            return profit[-1]
        else:
            return 0
        
