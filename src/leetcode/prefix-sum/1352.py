class ProductOfNumbers:

    def __init__(self):
        self.total = 0
        self.products = [1] # Calculate a prefix product of each element pushed into the list

    def add(self, num: int) -> None:
        # Reset the list of products when a 0 is reached since it would otherwise cause all future products to be 0
        if num == 0:
            self.products = [1] 
        else:
            self.products.append(self.products[-1] * num) # Push the new product onto the product sum list `products`

    def getProduct(self, k: int) -> int:
        # There must be a at least `k` elements pushed onto the `products` list
        if len(self.products) <= k:
            return 0
        else:
            # To find the product of the last `k` elements divide the `kth` element from the end from the product of the most recent element
            return self.products[-1] // self.products[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
