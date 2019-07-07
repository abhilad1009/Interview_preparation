"""
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?

"""
MEMORY_LIMIT=5

class File_to_save(object):
    def __init__(self):
        self.requests=[]
        self.start=None
        self.end=None
    

class HitCounter(object):

    def __init__(self):
        self.openfile=File_to_save()
        self.saved=[]



    def record(self,timestamp):
        if self.openfile.start==None:
            self.openfile.start=timestamp
        
        self.openfile.requests.append(timestamp)
        self.openfile.end=timestamp

        if len(self.openfile.requests)==MEMORY_LIMIT:
            self.saved.append(self.openfile)
            self.openfile=File_to_save()

    def total(self):
        return (len(self.saved)*MEMORY_LIMIT)+len(self.openfile.requests)

    def range(self,lower,upper):
        files=self.saved+[self.openfile]
        l=0
        r=MEMORY_LIMIT
        L=0
        R=len(files)-1
        for i in range(len(files)):
            if files[i].start<=lower and files[i].end>=lower:
                L=i
            if files[i].start<=upper and files[i].end>=upper:
                R=i

        for i in range(MEMORY_LIMIT):
            if files[L].requests[i]>=lower:
                l=i
                break
        for i in range(MEMORY_LIMIT):
            if files[R].requests[i]>upper:
                r=i-1
                break

        mid=(R-L-1)*MEMORY_LIMIT
        left=MEMORY_LIMIT-l
        right=r+1
        total=left+mid+right
        
        return total


hitter=HitCounter()

for i in range(59):
    hitter.record(i)

print(hitter.total())
print(hitter.range(7,27))