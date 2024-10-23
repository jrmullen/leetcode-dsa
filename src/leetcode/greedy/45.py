class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        l = r = 0 # 2 pointers `l` and `r` beginning at index 0

        # Simplified BFS over the `nums` list
        while r < len(nums) - 1:
            # Iterate over each element in the window between `l` and `r` to find the maximum possible jump height
            farthestJumpIdx = 0
            for i in range(l, r + 1):
                farthestJumpIdx = max(farthestJumpIdx, i + nums[i])
            
            # Update pointers to get the next window
            l = r + 1
            r = farthestJumpIdx
            result += 1 # Each new window is 1 jump, so increase the `result` counter
        
        return result
