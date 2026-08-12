# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        self.head=head
        l=set()
        if head==None:
            return False
        curr=self.head
        a=0
        while a==0:
            if curr in l:
                return True
            if curr.next==None:
                return False
            else:
                l.add(curr)
                curr=curr.next
