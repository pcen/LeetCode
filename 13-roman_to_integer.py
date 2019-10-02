val = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    
def romanToInt(s):
    decimal = 0
    it = enumerate(s)
    for i, n in it:
        if i + 1 != len(s):
            if val[n] < val[s[i + 1]]:
                decimal += val[s[i + 1]] - val[n]
                next(it)
            else:
                decimal += val[n]
        else:
            decimal += val[n]
    return decimal


print(romanToInt('XXIV') # 24 in roman numerals
