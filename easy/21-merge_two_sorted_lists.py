class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val <= l2.val:
        ret = ListNode(l1.val)
        l1 = l1.next
    else:
        ret = ListNode(l2.val)
        l2 = l2.next
    
    n = ret # iterator node
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            n.next = ListNode(l1.val)
            l1 = l1.next
        else:
            n.next = ListNode(l2.val)
            l2 = l2.next
        n = n.next
    
    if l1 is not None:
        n.next = l1
    else:
        n.next = l2
    
    return ret
