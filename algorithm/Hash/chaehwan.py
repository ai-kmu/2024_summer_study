class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chs = []
        cnt = 0
        maximum = 0
        for ch in s:
            if ch not in chs:
                chs.append(ch)
                cnt += 1
                if maximum < cnt:
                    maximum = cnt
                print(chs, maximum)
            else:
                chs = chs[chs.index(ch)+1:]
                chs.append(ch)
                cnt = len(chs)
                print(chs, cnt)

        return maximum
