from collections import defaultdict 
from random import randint
import copy
class GraphPainting:

    def __init__(self):
        self.graph = defaultdict(list)
        self.nodesColors = defaultdict(list)

    def setEdges(self):
        self.addEdge(0, 2)
        self.addEdge(0, 3)
        self.addEdge(1, 2)
        self.addEdge(1, 5)
        self.addEdge(2, 6)
        self.addEdge(3, 4)
        self.addEdge(3, 6)
        self.addEdge(4, 7)
        self.addEdge(5, 6)
        self.addEdge(5, 8)
        self.addEdge(6, 7)
        self.addEdge(7, 10)
        self.addEdge(8, 9)
        self.addEdge(9, 10)

        self.addEdge(1, 4)
        self.addEdge(0, 8)
        self.addEdge(1, 10)
        self.addEdge(0, 10)
        


    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def setColor(self, v, color):
        self.nodesColors[v].append(color)

    def getColor(self, v):
        return self.nodesColors[v]
    
    def getCurrentState(self):
        cs = defaultdict(list)
        cs = self.nodesColors
        return cs
    
    def setCurrentState(self, state):
        self.nodesColors = state

    def getNeighbors(self):
        actions = []
        for i in range(0, len(self.nodesColors)):
            if self.nodesColors[i] == ['R'] :
                actions.append([i, 'G'])
                actions.append([i, 'B'])
            elif self.nodesColors[i] == ['G']:
                actions.append([i, 'R'])
                actions.append([i, 'B'])
            else:
                actions.append([i, 'R'])
                actions.append([i, 'G'])
        return actions

    def getInitialState(self):
        for i in range(0, len(self.graph)):
            j = randint(0, 2)
            if j == 0:
                self.setColor(i, 'R')
            elif j == 1:
                self.setColor(i, 'G')
            elif j == 2:
                self.setColor(i, 'B')                

        return self.nodesColors


    def getRandomChromosome(self):
        chromosome = defaultdict(list)
        for i in range(0, len(self.graph)):
            j = randint(0, 2)
            if j == 0:
                chromosome[i].append('R')
            elif j == 1:
                chromosome[i].append('G')
            elif j == 2:
                chromosome[i].append('B')                

        return chromosome


    def nextState(self, currentState, action):
        cs = copy.deepcopy(currentState)
        cs[action[0]] = [action[1]]
        return cs

    def getObjectiveFunction(self, nodesColors):
        sameNeighborsColor = 0
        for i in range(0, len(self.graph)):
            for j in self.graph[i]:
                if nodesColors[i] == nodesColors[j]:
                    sameNeighborsColor = sameNeighborsColor + 1
        return float(-1 * sameNeighborsColor)/20

