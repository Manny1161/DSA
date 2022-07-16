from DSALinkedList import DSALinkedList
from DSAQueueList import DSAListQueue
from DSAStackList import DSAListStack
import numpy as np
class DSAGraphNode:
    def __init__(self, label, value):
        self._label = label
        self._value = value
        self._adjacent = DSALinkedList()
        self._visited = False

    @property
    def label(self):
        return self._label

    @property
    def value(self):
        return self._value

    @property
    def adjacent(self):
        return self._adjacent

    def addEdge(self, vertex):
        self._adjacent.insertFirst(vertex)

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, visited):
        self._visited = bool(visited)

    def __str__(self):
        return ("{label},{value}:{adj}"
                .format(label=self.label, value=self.value,
                        adj=" ".join([x.label for x in self.adjacent])))

    def gv(self):
        return "".join([f"{self.label} -- {x.label}\n" for x in self.adjacent])

    def __eq__(self, other):
        return self.label == other.label

class DSAGraph:
    def __init__(self):
        self._verticies = DSALinkedList()

    def addNode(self, label, value):
        self._verticies.insertFirst(DSAGraphNode(label, value))

    def addEdge(self, label1, label2):
        node1 = self.getNode(label1)
        node2 = self.getNode(label2)
        node1.addEdge(node2)
        node2.addEdge(node1)

    def hasNode(self, label):
        return self._verticies.find(DSAGraphNode(label, None))

    def countNode(self):
        return self._verticies.count()

    def countEdge(self):
        ## assumes an undirected graph ##
        return sum(x.adjacent.count() for x in self._verticies) // 2

    def getNode(self, label):
        # Use list internals for efficiency
        return self._verticies._find(DSAGraphNode(label, None))._data

    def getAdjacent(self, label):
        return self.getNode(label).adjacent

    def isAdjacent(self, label1, label2):
        return self.getNode(label1).adjacent.find(DSAGraphNode(label2, None))

    def displayAsList(self):
        return "".join(f"{x}\n" for x in self._verticies)

    def displayAsMatrix(self):
        label = [str(x.label) for x in self._verticies]
        col = len(max(label, key=lambda x: len(x))) + 1
        matrix = ' ' * col
        matrix += "".join([x + " " * (col-len(x)) for x in label])
        matrix += "\n"
        adjMatrix = self.adjacencyMatrix()
        for i, l in enumerate(label):
            matrix += l + " " * (col-len(l))
            matrix += (" " * (col-1)).join([str(x) for x in adjMatrix[i].flat])
            matrix += "\n"
        return matrix

    def adjacencyMatrix(self):
        count = self.countNode()
        m = np.zeros([count, count], dtype=int)
        for i, v in enumerate(self._verticies):
            for j, l in enumerate(self._verticies):
                m[i][j] = 1 if v.adjacent.find(l) else 0
        return m

    def display(self):
        return "graph {\n" + "".join([x.gv() for x in self._verticies]) + "}\n"
 
    def depthFirstSearch(self):
        # Mark nodes as new
        tree = DSAGraph()
        stack = DSAListStack()
        for v in self._verticies:
            v.visited = False

        # Set up first node
        if self._verticies._head is not None:
            head = self._verticies.peekFirst()
            head.visited = True
            tree.addNode(head.label, head.value)
            stack.push(head)
        
        # Perform DFS
        while not stack.isEmpty():
            node = next((x for x in stack.top().adjacent if not x.visited), None)
            if node is None:
                stack.pop()
            else:
                node.visited = True
                tree.addNode(node.label, node.value)
                tree.addEdge(node.label, stack.top().label)
                stack.push(node)
        return tree

    def breadthFirstSearch(self):
        tree = DSAGraph()
        queue = DSAListQueue()
        for v in self._verticies:
            v.visited = False
        
        if self._verticies._head is not None:
            head = self._verticies.peekFirst()
            head.visited = True
            tree.addNode(head.label, head.value)
            queue.enqueue(head)
        
        # Perform DFS
        while not queue.isEmpty():
            centre = queue.dequeue()
            for v in centre.adjacent:
                if not v.visited:
                    queue.enqueue(v)
                    tree.addNode(v.label, v.value)
                    tree.addEdge(centre.label, v.label)
                    v.visited = True
        return tree
    
    @staticmethod
    def readGraphFile(filename):
        graph = DSAGraph()
        with open(filename, "r") as f:
            for l in f:
                l1, l2 = l.rstrip("\n").split(" ")
                if not graph.hasNode(l1):
                    graph.addNode(l1, None)
                if not graph.hasNode(l2):
                    graph.addNode(l2, None)
                graph.addEdge(l1, l2)
        return graph

if __name__ == "__main__":
    graph1 = DSAGraph().readGraphFile("prac6_1.al")
    graph2 = DSAGraph().readGraphFile("prac6_2.al")
    '''graph = DSAGraph()
    graph.addNode('1', 'one')
    graph.addNode('2', 'two')
    graph.addNode('3', 'three')
    graph.addNode('4', 'four')
    graph.addEdge('1', '2')
    graph.addEdge('2', '3')
    graph.addEdge('4', '2')
    print(graph.hasNode('1'))
    print(graph.countNode())
    print(graph.isAdjacent('1', '2'))
    print(graph.countEdge())
    print(graph.displayAsList())'''
    print(graph1.depthFirstSearch().displayAsList())
    #print(graph2.breadthFirstSearch().displayAsList())