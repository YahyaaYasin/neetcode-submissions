class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        book = {}

        # base case
        if len(strs) <= 1:
            return [strs]

        # main 
        for string in strs:

            charCount = [0] * 26

            for char in string:
                charCount[ord(char) - ord("a")] += 1
            
            key = tuple(charCount)
            
            if key not in book:
                book[key] = [string]
            else:
                book[key].append(string)

        
        return list(book.values())


        
        
        