class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #use a set. keep interating the set with the list items. if the item already in the set, return true, ie,
        # there is a repeating item. other wise just add the item into the set

        s = set()

        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        
        return False

