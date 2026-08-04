class MyHashSet(object):
    def __init__(self):
        self.a=[]  
    def add(self, key):
        if key not in self.a:
            self.a.append(key) 
    def remove(self, key):
        d=None
        for i in range(len(self.a)):
            if self.a[i]==key:
                d=i
        if d!=None:
            del self.a[d]        
    def contains(self, key):
        if key in self.a:
            return True
        else:
            return False
