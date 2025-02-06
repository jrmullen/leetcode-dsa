class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        result = 0
        products = defaultdict(int)

        # Consider each pair of elements (i, j)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l = nums[i]
                r = nums[j]
                
                # Map the pair to their product
                products[l * r] += 1
            
        for count in products.values():
            pairs = (count * (count - 1)) // 2 # Split the tuples sharing a product into pairs
            result += 8 * pairs # Each pair has 8 possible tuple combinations
        
        return result
