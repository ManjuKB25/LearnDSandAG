class Node:

    def __init__(self):
        self.next = None
        self.data = None

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getCurr(self):
        return self

    def printNode(self):
        return "Current :: {0:s}, data :: {1:d}, next :: {2:s}".format(str(self), self.data, str(self.next))
        #return "data {0:d} next {1:s}".format(self.data, str(self.next))

newNode = Node()
newNode.setData(5)
#newNode.setNext(newNode)
print(newNode.printNode())
