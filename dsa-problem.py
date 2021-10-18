class Node: 
    def __init__(self,name,value,step):
        self.name = name
        self.value = value
        self.step = step
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
n = int(input("Number of steps: "))
n = n+1
x = input("Enter space seperated step numbers: ")
x = x.split(" ")
x = [int(i) for i in x]
x = list(set(x))
unExplored = []
finalNodes = []
root = Node(0,0,"")
counter = 1

def checkFinal():
    global finalNodes
    if len(finalNodes) == 0:
        print("No possible steps")
    else:
        finalSteps = []
        for i in finalNodes:
            finalSteps.append(i.step)
            # print(i.step)
        print(set(finalSteps))


def stepFunction(parent):
    global n
    global unExplored
    global finalNodes
    global counter

    for i in x:
        if((parent.value+i)<n):
            a = Node(counter,(parent.value+i),(parent.step+str(i)))
            counter = counter + 1
            parent.add_child(a)
            # print("Val is ",a.value)
            if(a.value==n-1):
                finalNodes.append(a)
            else:
                unExplored.append(a)
    
    if len(unExplored)!=0:
        newParent = unExplored[-1]
        unExplored.pop()
        stepFunction(newParent)
    else:
        checkFinal()

stepFunction(root)