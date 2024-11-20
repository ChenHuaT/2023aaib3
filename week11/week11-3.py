class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans, total = 0,0
        counter = Counter()
        for i in range(k): #取出前面K個數字
            num = nums[i]
            counter[num] += 1
            total += num
        if len(counter)==k: ans = max(ans, total)
        #上面只處理第一組毛毛蟲，下面要處理後續
        for i in range(k,len(nums)):
            left,right = nums[i-k], nums[i]
            counter[left] -= 1 #減左邊(舊)
            counter[right] += 1 #加右邊(新)
            total = total - left + right #減左邊(舊)、加右邊(新)
            if counter[left]==0: del counter[left]
            if len(counter)==k: ans = max(ans, total)
        return ans
