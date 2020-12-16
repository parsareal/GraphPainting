from graph import GraphPainting
from fcHillClimbing import fchcSearch

graphPainting = GraphPainting()
fchc = fchcSearch(graphPainting)
graphPainting.setEdges()
initialState = graphPainting.getInitialState()
# print initialState
# print graphPainting.getObjectiveFunction(initialState)
fchc.localSearch()