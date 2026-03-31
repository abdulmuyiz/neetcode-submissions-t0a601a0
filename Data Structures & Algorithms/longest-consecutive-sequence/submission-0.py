class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        nums.sort()
        result = 1
        check = 1
        pre = nums[0]
        for i in range(1,len(nums)):
            print(check)
            if pre == nums[i]:
                continue
            if pre+1 == nums[i]:
                check += 1
            else:
                if (check>result):
                    result = check
                check = 1
            pre = nums[i]

        if (check>result):
            result = check 
        return result