from graph import GraphPainting
from rrHillClimbing import rrhcSearch
import copy

graphPainting = GraphPainting()
rrhc = rrhcSearch(graphPainting)
graphPainting.setEdges()
initialState = graphPainting.getInitialState()
# print initialState
# print graphPainting.getObjectiveFunction(initialState)
finalFit = copy.deepcopy(rrhc.localSearch())

while finalFit != float(0):
    graphPainting.getInitialState()
    finalFit = copy.deepcopy(rrhc.localSearch())

rrhc.getResult()
