from graph import GraphPainting
from rrHillClimbing import rrhcSearch

graphPainting = GraphPainting()
rrhc = rrhcSearch(graphPainting)
graphPainting.setEdges()
initialState = graphPainting.getInitialState()
# print initialState
# print graphPainting.getObjectiveFunction(initialState)
rrhc.localSearch()
rrhc.getResult()