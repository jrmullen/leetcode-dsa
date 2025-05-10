class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0 # Track the total sum of each list
        sum2 = 0
        count1 = 0 # Count number of 0s in each list
        count2 = 0

        # Calculate the total sum of each list and count the number of zeroes
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                sum1 += nums1[i] if nums1[i] > 0 else 1 # 
                count1 += 1 if nums1[i] == 0 else 0

            if i < len(nums2):
                sum2 += nums2[i] if nums2[i] > 0 else 1
                count2 += 1 if nums2[i] == 0 else 0

        # Base case: the sums are different, and there are no available zeroes to fill to make the smaller value larger
        if (count1 == 0 and sum2 > sum1) or (count2 == 0 and sum1 > sum2):
            return -1 # It is impossible to make the sums equal

        return max(sum1, sum2) # Whichever value is larger will be the minimum possible sum
