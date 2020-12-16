import copy
from random import randint
from collections import defaultdict 
import matplotlib.pyplot as plt

class Genetic:
     
    def __init__(self, problem, populationSize, tornumentSize, mutationRate, numberOfGenerations):
        self.problem = problem
        self.populationSize = populationSize
        self.tornumentSize = tornumentSize
        self.mutationRate = mutationRate
        self.numberOfGenerations = numberOfGenerations
        self.bestPerEachGen = []
        self.worstPerEachGen = []
        self.meanPerEachGen = []

        
    
    def initialPopulation(self):
        population = []
        populationSize = copy.deepcopy(self.populationSize)
        while populationSize != 0:
            chromosome = copy.deepcopy(self.problem.getRandomChromosome())
            population.append(chromosome)
            populationSize -= 1
        return population
    
    def fitnessChromosome(self, chromosome):
        return -1 * self.problem.getObjectiveFunction(chromosome)

    def tornument(self, population):
        index = 0
        chosenChromosomes = []
        bestForGen = 0
        worstForGen = 2
        mean = 0
        while index != self.populationSize:
            bestFit = 0
            bestOne = copy.deepcopy(population[index])

            for i in range(index, index + self.tornumentSize):
                mean += self.fitnessChromosome(population[i])
                # print i, '   ',self.fitnessChromosome(population[i]) 

                if (self.fitnessChromosome(population[i]) > bestFit):
                    bestOne = copy.deepcopy(population[i])
                    
                if (self.fitnessChromosome(population[i]) > bestForGen):
                    bestForGen = copy.deepcopy(self.fitnessChromosome(population[i]))

                if (self.fitnessChromosome(population[i]) < worstForGen):
                    worstForGen = copy.deepcopy(self.fitnessChromosome(population[i]))

            chosenChromosomes.append(bestOne)
            index += self.tornumentSize

        # print mean
        # print self.populationSize
        # print 'BEST_GEN: ', bestForGen
        # print 'WORST_GEN: ', worstForGen
        # print 'MEAN_GEN: ', float(mean)/self.populationSize

        self.bestPerEachGen.append(bestForGen)
        self.worstPerEachGen.append(worstForGen)
        self.meanPerEachGen.append(float(mean)/self.populationSize)

        return chosenChromosomes

    def newGeneration(self, chosenChromosomes):
        childNum = 0
        newGeneration = []
        while childNum != self.populationSize:
            rand1 = randint(0, len(chosenChromosomes) - 1)
            rand2 = randint(0, len(chosenChromosomes) - 1)
            # print chosenChromosomes[rand2]
            newChild = self.crosover(chosenChromosomes[rand1], chosenChromosomes[rand2], len(chosenChromosomes[rand1]))
            newGeneration.append(newChild)
            childNum += 1
        return newGeneration


    def crosover(self, ch1, ch2, n):
        rand = randint(0, n-1)
        newChild = defaultdict(list)
        for i in range(0, rand):
            newChild[i] = ch1[i]
        for i in range(rand, n):
            newChild[i] = ch2[i]   
        return newChild
    
    def mutation(self, n, generation):
        newGeneration = copy.deepcopy(generation)
        mutatedGenomes = len(newGeneration) * n * self.mutationRate
        while mutatedGenomes > 0:
            randomChromosome = randint(0, len(newGeneration) - 1)
            randomNode = randint(0, n-1)
            randomColor = randint(0, 2)
            chromosome = newGeneration[randomChromosome]
            
            if randomColor == 0:
                chromosome[randomNode] = ['R']
            elif randomColor == 1:
                chromosome[randomNode] = ['G']
            elif randomColor == 2:
                chromosome[randomNode] = ['B']
            mutatedGenomes -= 1
        return newGeneration


    def plot(self, number_of_generations):
        generations = []
        for i in range(0, number_of_generations):
            generations.append(i)
        plt.plot(generations, self.bestPerEachGen, label='Maximums', c='r')
        plt.plot(generations, self.meanPerEachGen, label='Averages', c='b')
        plt.plot(generations, self.worstPerEachGen, label='Minimums', c='g', linewidth=2)

        plt.xlabel('Generations')
        plt.ylabel('Costs')
        title = ['Generations: {0}'.format(number_of_generations) + ' - Population Size: {0}'.format(self.populationSize),
                 'Tournament Size: {0}'.format(self.tornumentSize) + ' - Mutation Rate: {0}'.format(self.mutationRate)]
        plt.title('\n'.join(title))
        plt.legend()

        plt.savefig('-'.join(title).replace(':', '') + '.png')
        plt.show()