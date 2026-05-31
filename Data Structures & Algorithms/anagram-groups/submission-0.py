class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        lenindx = len(strs) - 1

        for item in strs:
            samplelst = list(item)
            samplelst.sort()

            s = ''
            for i in samplelst:
                s += i

            if not s in result:
                result[s] = [item]
            else:
                result[s].append(item)

        return list(result.values())


        