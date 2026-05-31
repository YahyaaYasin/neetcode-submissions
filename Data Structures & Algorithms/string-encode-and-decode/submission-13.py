class Solution:

    def encode(self, strs: List[str]) -> str:

        # init a string 
        out = ""
        str_left = len(strs) - 1

        # add all the string together with a -
        for string in strs:
            out += str(len(string))
            out += "#"
            out += string

        # return the string
        return out

    def decode(self, s: str) -> List[str]:

        out = []

        while s:
            j = s.index("#")        # find where '#' actually is
            _len = int(s[:j])       # length is everything before it
            s = s[j + 1:]           # skip past the '#'
            out.append(s[:_len])    # grab exactly _len chars
            s = s[_len:]            # advance

        return out

            
        
