class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        nums[:] = nums[-k:] + nums[:-k]
        

#Note : slicing in python 
# format 
#     nums[start:end]
# nums[:] means nums[0 to len(nums)] ie entire array or copy of the array
# positive and neg indices for an array :
#     Positive:  0  1  2  3  4  5  6
#     Value:     1  2  3  4  5  6  7
#     Negative: -7 -6 -5 -4 -3 -2 -1

#     so nums[-k:] or nums[-3:] means from (-3)rd index till end ie, from 4th index till end/6th
#     similarly, nums[:-3] means 0 to -3rd index or 4th index here. 


# now, arr[start:end:step] is the full syntax where
#     start = where to begin
#     end = where to stop (exclusive)
#     step = how many positions to move each time

# so, a[::1] means start at beginning of array, end at its end, take step as +1 so
# a=[1,2,3,4]
# will give same [1,2,3,4]

# now a[::2] will give Every second character ie [1,3]
# a[::3] will give [1,4]

# for negetive numbers as step: start = end of the array
#  end = start of the array
# a= [a,b,c,d,e]
#  a[::-1] gives [e,d,c,b,a] (reverse)
#  a[::-2] gives [e,c,a] etc.......