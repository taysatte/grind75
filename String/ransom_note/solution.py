
class Solution:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        magDict = dict()
        for s in range(0, len(magazine)):
            magDict[magazine[s]] = magDict.get(magazine[s], 0) + 1
        for i in range(0, len(ransomNote)):
            if ransomNote[i] in magDict.keys() and magDict.get(ransomNote[i]) > 0:
                magDict[ransomNote[i]] = magDict.get(ransomNote[i], 0) - 1
            else:
                return False
        return True
