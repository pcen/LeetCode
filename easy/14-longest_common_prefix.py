class Solution:
    
    def allSplicesEqual(self, lis, length):
        prefix = lis[0][:length]
        for e in lis:
            if length > len(e) or e[:length] != prefix:
                return False
        return True    
    
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        length = 1
        while(self.allSplicesEqual(strs, length)):
            length += 1
        ans = strs[0][:length - 1]
        if ans == 0:
            return ''
        return ans

py_things = ['python', 'pythonic', 'pythoner', 'pythonista', 'pythons are snakes', 'pythons fight pythons']
sol = Solution()
print(sol.longestCommonPrefix(py_things))
