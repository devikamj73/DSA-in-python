class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s) #Count occurrences of elements automatically.
        #output of this is freq = {'t':1, 'r':2, 'e': 2}

        result = ""

        for char, count in sorted(freq.items(),  key=lambda x: x[1], reverse = True):
            result = result + char*count
        #freq.items() will make it (key, value pairs), 
        #lambda parameter: expression is a general form to indicate how to use x
        # here x or x[0] is representing first part of the pair like e,t,r eyc 
        # x[1] indicates the next part i.e, freq
        # so key is taken as x[1] part i.e, frequency numbers are used for sorting
        #reverse because we need in descending order

        return result