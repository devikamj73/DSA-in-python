class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0

        for i in stones:
            if i in s:
                count += 1

        
        return count
        
# NOTE this problem is a classic example of optimization using set/hashset
# x in list takes O(n) time because Python may scan the entire list, while x in set takes O(1) average time due to hashing.
# Without a set, we would need a nested loop where every stone is compared against every jewel, resulting in a time complexity of O(m × n).
    # i.e, 
    # for stone in stones:
    #     for jewel in jewels:
# will have to compare each element from stone with every element in jewels, so O(n)

# in case of a set, it just have to check if that particular item exists at a particular space. so look up is 
# simply O(1)

#so in this solution, its O(n + m); O(m) to create set, then O(n) iterating through stones list
        
        