import copy
from random import randint
import random

class SASearch:

    def __init__(self, problem):
        self.problem = problem

    def localSearch(self):
        ts = 0
        expandedNodes = 0
        visitedNodes = 0

        while int(ts) != 1:
            actions = self.problem.getNeighbors()
            currentState = copy.deepcopy(self.problem.getCurrentState())
            # print 'currentState: ', currentState
            co = self.problem.getObjectiveFunction(currentState)
            rand = randint(0, len(actions)-1)
            choosedAction = actions[rand]
            nextState = self.problem.nextState(currentState, choosedAction)
            visitedNodes += 1
            no = self.problem.getObjectiveFunction(nextState)
            if no > co:
                self.problem.setCurrentState(nextState)
                expandedNodes += 1
            else:
                x = random.uniform(0, 1)
                if (x > ts):
                    self.problem.setCurrentState(nextState)
                    ts += 0.01
                    expandedNodes += 1

            
        print 'final: ',currentState, ' fitness: ', self.problem.getObjectiveFunction(currentState)
        print 'EXPANDED_NODES:  ', expandedNodes
        print 'VISITED_NODES:  ', visitedNodes