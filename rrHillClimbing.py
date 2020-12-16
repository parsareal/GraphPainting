from random import randint
import time
import copy

class rrhcSearch:

    def __init__(self, problem):
        self.problem = problem
        self.visitedNodes = 0
        self.expandedNodes = 0

    def localSearch(self):
        foundBetterState = True
        # self.state = initialState

        while foundBetterState:
            foundBetterState = False
            actions = self.problem.getNeighbors()
            currentState = copy.deepcopy(self.problem.getCurrentState())
            # print 'currentState: ', currentState
            co = self.problem.getObjectiveFunction(currentState)
            bso = copy.deepcopy(co)
            bestState = copy.deepcopy(currentState)
            # bestState = self.problem.nextState(currentState, actions[0])
            # bso = self.problem.getObjectiveFunction(bestState)
            
            for a in actions:
                # print 'action ', a
                # print 'currentState: ', currentState
                nextState = self.problem.nextState(currentState, a)
                self.visitedNodes += 1
                no = self.problem.getObjectiveFunction(nextState)
                # print 'nextState: ', nextState, '   no: ', no
                if no > bso:
                    bso = copy.deepcopy(no)
                    bestState = copy.deepcopy(nextState)
                    foundBetterState = True
                
            if foundBetterState:
                # print 'betters: ',betterStates
                self.expandedNodes += 1
                self.problem.setCurrentState(bestState)
        
        self.cs = copy.deepcopy(currentState)
        return self.problem.getObjectiveFunction(currentState)


    def getResult(self):
        print 'final: ',self.cs, ' fitness: ', self.problem.getObjectiveFunction(self.cs)
        print 'EXPANDED_NODES:  ', self.expandedNodes
        print 'VISITED_NODES:  ', self.visitedNodes
            
