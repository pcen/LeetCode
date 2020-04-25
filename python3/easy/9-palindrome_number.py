def isPalindrome_with_string(x):
    if x < 0:
        return False
    rev = ([d for d in str(x)])
    rev.reverse()
    rev = int(''.join(rev))
    return rev == x

def isPalindrome_without_string(x):
    if x < 0:
        return False
    q = x
    rev = 0
    while q != 0:
        r = q % 10
        q = q // 10
        rev = (10 * rev) + r
    return rev == x


print(isPalindrome_without_string(121))
print(isPalindrome_with_string(121))

print(isPalindrome_without_string(112))
print(isPalindrome_with_string(112))
