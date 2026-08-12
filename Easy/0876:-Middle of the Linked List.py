class Solution(object):
    def middleNode(self, head):
        self.head=head
        if self.head==None:
            return []
        else:
            curr=self.head
            count=0
            while curr!=None:
                curr=curr.next
                count+=1 
        current=self.head
        l=[]       
        if count%2==0:
            n=1
            while n!=(count//2)+1:
                current=current.next
                n+=1
        else:
            n=1
            while n!=(count//2)+1:
                current=current.next
                n+=1
        return current
