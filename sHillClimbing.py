from random import randint
import time
import copy

class shcSearch:

    def __init__(self, problem):
        self.problem = problem

    def localSearch(self):
        foundBetterState = True
        # self.state = initialState
        visitedNodes = 0
        expandedNodes = 0

        while foundBetterState:
            foundBetterState = False
            actions = self.problem.getNeighbors()
            currentState = copy.deepcopy(self.problem.getCurrentState())
            # print 'currentState: ', currentState
            co = self.problem.getObjectiveFunction(currentState)
            betterStates = []
            for a in actions:
                # print 'action ', a
                # print 'currentState: ', currentState
                nextState = self.problem.nextState(currentState, a)
                visitedNodes += 1
                no = self.problem.getObjectiveFunction(nextState)
                # print 'nextState: ', nextState, '   no: ', no
                if no > co:
                    betterStates.append(nextState)
                    foundBetterState = True
            
            if foundBetterState:
                expandedNodes += 1
                # print 'betters: ',betterStates
                rand = randint(0, len(betterStates)-1)
                self.problem.setCurrentState(betterStates[rand])
            
        print 'final: ',currentState, ' fitness: ', self.problem.getObjectiveFunction(currentState)
        print 'EXPANDED_NODES:  ', expandedNodes
        print 'VISITED_NODES:  ', visitedNodes
