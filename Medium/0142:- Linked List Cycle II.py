# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        self.head=head
        l=[]
        if self.head==None:
            return None
        else:
            i=head
            while i.next != None:
                if i not in l:
                    l.append(i)
                    i=i.next
                else:
                    return i
