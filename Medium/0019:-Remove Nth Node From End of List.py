# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next==None:
            return head.next
        count=0 
        current=head  
        while current!=None:
            current=current.next
            count+=1
        if count==n:
            return head.next
        curr=head
        m=1
        while m<(count-n):
            curr=curr.next
            m+=1
        if n==1:
            curr.next=None
        else:
            curr.next=curr.next.next
        return head


        
        
