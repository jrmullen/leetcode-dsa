class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        p1, p2 = 0, 0 # 2 pointers 

        while p1 < len(nums1) and p2 < len(nums2):
            id1, n1 = nums1[p1]
            id2, n2 = nums2[p2]
            
            if id1 == id2:
                # If the IDs are the same, add the sum of the values to the `result` list and move both pointers forward
                result.append([id1, n1 + n2])
                p1 += 1
                p2 += 1
            elif id1 < id2:
                # If the first ID is smaller, add it to the `result` list and move the `p1` pointer forward
                result.append(nums1[p1])
                p1 += 1
            else:
                # If the second ID is smaller, add it to the `result` list and move the `p2` pointer forward
                result.append(nums2[p2])
                p2 += 1
        
        # If there are any straggling pairs in `nums1`, add them to the `result` list
        while p1 < len(nums1):
            result.append(nums1[p1])
            p1 += 1

        # If there are any straggling pairs in `nums2`, add them to the `result` list
        while p2 < len(nums2):
            result.append(nums2[p2])
            p2 += 1
        
        return result
