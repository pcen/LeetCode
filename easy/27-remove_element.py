def removeElement(nums, val):
	ofst = 0
	index = 0
	length = 0
	for e in nums:
		if e == val:
			ofst += 1
		else:
			length += 1
			nums[index - ofst] = e			
		index += 1
	
	return length