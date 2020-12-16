from genetics import Genetic
from graph import GraphPainting
import copy
import matplotlib.pyplot as plt

populationSize = 100
tornumentSize = 10
mutationRate = 0.1
numberOfGenerations = 500
n = 11
nog = copy.deepcopy(numberOfGenerations)

graph = GraphPainting()
graph.setEdges()
genetic = Genetic(graph, populationSize, tornumentSize, mutationRate, numberOfGenerations)
initialPopulation = copy.deepcopy(genetic.initialPopulation())

while numberOfGenerations != 0:
    chosenChromosomes = genetic.tornument(initialPopulation)
    newGeneration = genetic.newGeneration(chosenChromosomes)
    finalGeneration = genetic.mutation(n, newGeneration)
    initialPopulation = copy.deepcopy(finalGeneration)
    numberOfGenerations -= 1

print finalGeneration
genetic.plot(nog)