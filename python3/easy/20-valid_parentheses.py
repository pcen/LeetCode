class Solution:
    
    pairs = { '(':')', '{':'}', '[':']' }

    def is_valid_pair(self, opening, closing):
        if not opening in self.pairs:
            return False
        if self.pairs[opening] == closing:
            return True
        return False
    
    def isOpen(self, c):
        return c in self.pairs.keys()
    
    def isValid(self, s):
        stack = []
        if len(s) == 0:
            return True
        for c in s:
            if self.isOpen(c):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop(-1)
                if not self.is_valid_pair(top, c):
                    return False
        if len(stack) > 0:
            return False
        return True

s = Solution()
test_string = '((((({}{}{}{}{}{}{}{}{}(()))))))[[[[[[[]]]]]]](([[[]]][]))'
print(s.isValid(test_string))
