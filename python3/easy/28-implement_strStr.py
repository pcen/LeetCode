def atSubstring(index, haystack, needle, len_needle):
	for i in range(index + 1, index + len_needle):
		if haystack[i] != needle[i - index]:
			return False
	return True

def strStr(haystack, needle):
	# return 0 for empty strings as do strstr() in C and indexOf() in Java
	if not needle or needle == "":
		return 0
	
	l_ndl = len(needle)
	l_hay = len(haystack)
	
	# return index of first needle or -1 if none are found
	for i in range(len(haystack)):
		if needle[0] == haystack[i] and (l_hay - i) >= l_ndl:
			if atSubstring(i, haystack, needle, l_ndl):
				return i
	return -1
