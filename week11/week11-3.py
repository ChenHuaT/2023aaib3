class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans, total = 0,0
        counter = Counter()
        for i in range(k): #���X�e��K�ӼƦr
            num = nums[i]
            counter[num] += 1
            total += num
        if len(counter)==k: ans = max(ans, total)
        #�W���u�B�z�Ĥ@�դ���ΡA�U���n�B�z����
        for i in range(k,len(nums)):
            left,right = nums[i-k], nums[i]
            counter[left] -= 1 #���(��)
            counter[right] += 1 #�[�k��(�s)
            total = total - left + right #���(��)�B�[�k��(�s)
            if counter[left]==0: del counter[left]
            if len(counter)==k: ans = max(ans, total)
        return ans
