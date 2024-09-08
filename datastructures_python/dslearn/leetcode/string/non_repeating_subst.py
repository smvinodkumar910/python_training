
string_val = 'au'

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = dict({'word':'','length':0})
        length = len(s)
        print(length)
        if length==0:
            return 0
        elif length==1:
            return 1
        else:
            for i in range(length):
                comp = ''
                for j in s[i+1:length]:
                    comp = comp+j
                    subst = s[i]+comp
                    if len(subst) != len(set(subst)):
                        break
                    else:
                        if len(subst)>output['length']:
                            output = { 'word':subst, 'length' : len(subst)}
                        continue
            return output['length']


    
        
solution = Solution()
print(solution.lengthOfLongestSubstring(string_val))
        
        