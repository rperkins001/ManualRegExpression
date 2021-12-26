
class BruteForceMagicRegex():

    def __init__(self):
        lst = input('Put in a line in: ').split()
        self.makedict(lst)
        self.comparedict(lst)
        self.setmatch(self.matches)
        self.maxval(self.matchdict)

    def makedict(self, l):
        self.dict = {}
        for i in l:
            listi = list(i)
            self.dict[i] = []

            for x in range(0, len(listi)):
                for y in range(x+1, len(listi)+1):
                    joinstr = (''.join(listi[x:y]))
                    self.dict[i].append(joinstr)

    def comparedict(self, l):
        x = 0
        self.matches = []
        
        while x < (len(l)-1):
            word1 = l[x]
            word2 = l[x+1]
            key1 = self.dict[word1]
            key2 = self.dict[word2]
            for i in (key1):
                for j in (key2):
                    if i == j and len(i)>1:
                        self.matches.append((word1, word2, i))
            x += 1
            
    def setmatch(self, l):
        self.matchdict = {}
        for (i,j,k) in l:
            if (i,j) not in self.matchdict:
               self.matchdict[(i,j)] = [k]
            else: 
               self.matchdict[(i,j)].append(k)
            
        
    def maxval(self, l):
        keys = l.keys()
        
        for i in keys:
            l[i] = max(l[i], key=len)
        
        print(l)
        

            



                    
        
        


         
    
        
        
        
            
BruteForceMagicRegex()


