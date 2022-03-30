class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=0
        for i in reversed(range(len(nums))):
            if nums[i]!=0:
                ind=i
                break
        i=j=0
        while i<ind-j:
            if nums[i]!=0:
                i+=1
            else:
                nums.append(nums.pop(i))
                j+=1
        return nums
