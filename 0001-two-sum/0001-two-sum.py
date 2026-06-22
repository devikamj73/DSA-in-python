class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {} # defining the hashmap h

        #adding items into hashmap
        for i in range(len(nums)):
            h[nums[i]] = i
        
        #finding the remaining value to be found in the list such that the sum of num[i] and 
        # that integer equals our target value.
        for i in range(len(nums)):
            y = target - nums[i]

            if y in h and h[y]!= i:
                return(i, h[y])
        