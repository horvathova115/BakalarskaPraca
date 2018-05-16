import math
from decimal import*

class IGmeasurement:

    def __init__(self,keys,values):
        
        self.keys=keys
        self.values=values
        self.informationGain()
        self.gainRatio()

    def entropy(self,i):
        dataEntropy=0.0
        val= self.values[i]
        for v in val:
            dataEntropy += (-float(v)/float(self.keys[i]))* math.log(float(v)/float(self.keys[i]),2)
        return dataEntropy
    

    def informationGain(self):
        sumEnt=0.0
        for i in range(1,len(self.keys)):
            sumEnt+=(float(self.keys[i])/float(self.keys[0]))* self.entropy(i)
##        print(sumEnt)
        ig=self.entropy(0)- sumEnt
##        print("ig", ig)
        return ig

    def splitInfo(self):
        si=0.0
        for i in range(1,len(self.keys)):
            si+=(-float(self.keys[i])/float(self.keys[0]))* math.log(float(self.keys[i])/float(self.keys[0]),2)
                   
        return si    

    def gainRatio(self):
        
        gr= self.informationGain()/self.splitInfo() 
##        print ("gr",gr)
        return gr

catValues=[[22,17,21],[2,6,4],[13,5,9],[5,1,2],[2,5,6]]
catKeys=[60,12,27,8,13]
resultValues =[[21,18,21],[1,6,3],[2,1,4],[6,2,1],[2,2,4],[4,1,1],[1,3],[1,4,3],[5,1],[2]]
resultKeys=[60,10,7,9,8,6,4,8,6,2]

label=["A","L","P","U"]
i=0
##k=[0,0,0,0]
##v=[0,0,0,0]
Sdata={81:[28,25,28]}
data=[{17:[4,8,5],64:[24,16,23]},{17:[3,5,9], 22:[14,3,5],42:[11,17,14]}, {9:[1,5,3],5:[1,4],67:[27,19,21]},{7:[6,1],4:[2,2],70:[22,22,26]}]
for d in data:
    print(label[i])
    
    k=Sdata.keys()
    for x in d.keys():
        k.append(x)
    
##    print(k)
    v=(Sdata.values())
    for j in d.values():
        v.append(j)
##    print(v)
    
    IG=IGmeasurement(k,v)
    i+=1
    print("IG",IG.informationGain())
    print("GR", IG.gainRatio())
