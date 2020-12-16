from graph import GraphPainting
from sHillClimbing import shcSearch

graphPainting = GraphPainting()
shc = shcSearch(graphPainting)
graphPainting.setEdges()
initialState = graphPainting.getInitialState()
# print initialState
# print graphPainting.getObjectiveFunction(initialState)
shc.localSearch()