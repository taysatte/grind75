class Solution:
    
    def twoSumBrute(self, pList: list[int], pTarget: int) -> list[int]:
        for i in range(0, len(pList)):
            comp = pTarget - pList[i]
            for j in range(i, len(pList)):
                if comp == pList[j] and i != j:
                    return [i, j]
    
    def twoSumDict(self, pList: list[int], pTarget: int) -> list[int]:
        compDict = {}
        for i in range(0, len(pList)):
            comp = pTarget - pList[i]
            if pList[i] in compDict:
                return [compDict[pList[i]], i]
            else:
                compDict[comp] = i
