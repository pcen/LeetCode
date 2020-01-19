def printList(head):
	while head is not None:
		if head.next:
			print(head.val, " -> ", end="")
		else:
			print(head.val)
		head = head.next

def buildLL(vals):
	if not vals:
		return None
	head = ListNode(vals[0])
	_head = head
	_vals = iter(vals)
	next(_vals)
	for v in _vals:
		head.next = ListNode(v)
		head = head.next
	return _head

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def addTwoNumbers(l1, l2):
	ret = n = ListNode(0)
	c = 0
	while l1 or l2 or c > 0:
		(val1, l1) = (l1.val, l1.next) if l1 else (0, None)
		(val2, l2) = (l2.val, l2.next) if l2 else (0, None)
		net_sum = val1 + val2 + c
		next_val, c = net_sum % 10, net_sum // 10
		n.next = n = ListNode(next_val)
	return ret.next
