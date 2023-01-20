def productExceptSelf(nums):
    answer = [1] * len(nums)

    # Populate left-side products
    pre = 1
    for i in range(len(nums)):
        answer[i] = pre
        pre *= nums[i]

    # Populate right-side products
    post = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= post
        post *= nums[i]

    return answer

def main():
    productExceptSelf([1,2,3,4])

if __name__ == "__main__":
    main()