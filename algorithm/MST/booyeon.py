# timeout 상당히 나이브한 풀이. mst로 다시 풀 예정


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 1. pairs를 걸으면서 이미 수집한 무리의 값을 pair중 하나라도 가지고 있으면 무리에 포함 아니면 불포함. 
        # 2. 그렇게 얻은 무리의 string을 순서에따라 정렬
        # 3. 해당 무리에 배정된 자리값대로 배열 해서 완성

        # 1
        connectedPairElementGroup = []

        for pair in pairs:
            isUnique = True
            for pairGroup in connectedPairElementGroup:
                for i in range(2):
                    if pair[i] in pairGroup:
                        tmp = pairGroup + [pair[(i+1)%2]]
                        for idx in range(len(connectedPairElementGroup)-1,-1,-1):
                            pairGroupAgain = connectedPairElementGroup[idx]
                            for e in tmp:
                                if e in pairGroupAgain:
                                    tmp.extend(pairGroupAgain)
                                    connectedPairElementGroup.remove(pairGroupAgain)
                                    break
                        connectedPairElementGroup.append(list(set(tmp)))
                        isUnique = False
                        break
                if not(isUnique): break
            if isUnique:
                connectedPairElementGroup.append(pair)

                
        
        # 2
        sList = list(s)

        for group in connectedPairElementGroup:
            group.sort()
            for iIdx, char in enumerate(sorted([s[eIdx] for eIdx in group])):  # 3
                sList[group[iIdx]] = char

        return ''.join(sList)

        

