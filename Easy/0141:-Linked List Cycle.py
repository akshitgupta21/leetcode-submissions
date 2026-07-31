# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        self.head=head
        l=set()
        if self.head==None:
            return False
        else:
            curr=head
            while curr.next!=None:
                if curr not in l:
                    l.add(curr)
                    curr=curr.next
                else:
                    return True
