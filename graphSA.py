from graph import GraphPainting
from sAnealing import SASearch
import random

graphPainting = GraphPainting()
sa = SASearch(graphPainting)
graphPainting.setEdges()
initialState = graphPainting.getInitialState()
print graphPainting.getObjectiveFunction(initialState)
sa.localSearch()
# x = random.uniform(0, 1)
# print x