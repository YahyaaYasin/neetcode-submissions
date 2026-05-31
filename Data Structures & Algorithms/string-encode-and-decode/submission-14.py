class Solution:

    def encode(self, strs: List[str]) -> str:

        # init a string 
        out = ""
        str_left = len(strs) - 1

        # add all the string together int the format <length#string>
        for string in strs:
            out += str(len(string))
            out += "#"
            out += string

        # return the string
        return out

    def decode(self, s: str) -> List[str]:

        # init a string 
        out = []

        while s:

            # Find where is the hastag
            j = s.index("#")

            # length is everything before it
            _len = int(s[:j])       
            
            # skip past the '#'
            s = s[j + 1:]           
            
            # grab exactly _len chars
            out.append(s[:_len])    
            
            # next
            s = s[_len:]            

        return out

            
        
