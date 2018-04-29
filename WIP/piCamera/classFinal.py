import math

class edge:
    def __init__(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setWeight(self, v):
        self.weight = v

class node:
    def __init__(self, bias, ID, aType = 'step'):
        self.bias = bias
        self.inputs = []
        self.weights = []
        self.aType = aType
        self.out = 0
        self.ID = ID

    def setInputs(self, inputs):
        self.inputs = inputs

    def actFunction(self, p):
        if self.aType == 'step':
            if p > 0:
                return 1
            else:
                return 0

    def activateAsOutput(self):
        p = 0
        for i in range(len(self.weights)):
            p += self.weights[i] * self.inputs[i]
        self.out = self.actFunction(p + self.bias)

    def activateAsInput(self):
        self.out = self.inputs
        return self.out

    def getBias(self):
        return self.bias

    def setWeights(self, weight):
        self.weights.append(weight)

    def __str__(self):
        return str(self.ID)

class network:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.outputNodes = []
        self.inputNodes = []

    def addNode(self, ID, bias):
        self.nodes[ID] = (node(bias, ID))

    def inputToNode(self, ID, inputVal):
        self.nodes[ID].setInputs(inputVal)

    def getAllNodes(self):
        return self.nodes

    def getBiasNode(self, ID):
        return self.nodes[ID].getBias()

    def connectEdge(self, tar, src, weight):
        self.target = (tar)
        self.src = (src)
        # Try catch so first connection defines target in dictionary, all others are only appended
        try:
            self.edges[self.target]
        except:
            self.edges[self.target] = []
        self.edges[self.target].append(self.src)
        self.nodes[self.target].setWeights(weight)

    def getEdges(self, tar):
        # Returns Connections based on passed target
        target = str(tar)
        try:
            self.edges[target]
        except:
            return "Undefined Target"
        return self.edges[target]

    def setOutputNodes(self, outputs):
        self.outputNodes = outputs

    def setInputNodes(self, inputs):
        self.inputNodes = inputs

    def getInput(self):
        return self.inputs

    def step(self):
        val = []
        for i in (self.inputNodes):
            i = str(i)
            val.append(self.nodes[i].activateAsInput())
        for i in (self.outputNodes):
            i = str(i)
            self.inputToNode(i, (val))
            self.nodes[i].activateAsOutput()

    def getOut(self):
        ret = []
        for i in (self.outputNodes):
            i = str(i)
            ret.append(self.nodes[i].out)
        return ret

if __name__ == "__main__":
    print "foo"
