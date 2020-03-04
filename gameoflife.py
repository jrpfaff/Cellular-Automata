import copy
import random
from matplotlib import pyplot as plt


def BuildGrid(rows, cols):
    '''Creates the grid and dummy grid to be used to hold to automata.'''
    Grid = []
    if rows <= 0:
        return Grid
        cols = rows
    if cols <= 0:
        cols = rows

    for i in range(rows):
        Grid.append([])
    for j in Grid:
        for k in range(cols):
            j.append(0)
    DummyGrid = copy.deepcopy(Grid)
    return Grid, DummyGrid

def SumofAdjacent(Grid, i, j):
    '''Calculates the number of neighbors of a given entry in the grid,
     will be used to determine if the entry lives or dies in the next generation.'''
    if i < 0 or j < 0 or i >= len(Grid) or j >= len(Grid[0]):
        print("Invalid Coordinates")
        return 0

    cols = len(Grid[0])
    rows = len(Grid)
    sum = -1*Grid[i][j]

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            try:
                a = i + x
                b = j + y
                if b >= 0 and a >= 0:
                    sum += Grid[a][b]
            except Exception as e:
                sum += 0

    return sum


def UpdateGrid(Grid, NewGrid):
    '''Calculates the number of neighbors for each point in the grid and makes
    the grid for the next generation'''

    for i in range(len(Grid)):
        for j in range(len(Grid[0])):
            NumNeighbors = SumofAdjacent(Grid, i, j)
            if Grid[i][j] == 1:
                if NumNeighbors < 2:
                    NewGrid[i][j] = 0
                elif NumNeighbors == 2 or NumNeighbors == 3:
                    NewGrid[i][j] = 1
                else:
                    NewGrid[i][j] = 0
            else:
                if NumNeighbors == 3:
                    NewGrid[i][j] = 1
                else:
                    NewGrid[i][j] = 0

    Grid = NewGrid
    return NewGrid

def RunAutomata(Grid, NewGrid, NumIterations):
    '''Draws the grid using Pyplot and updates to the next generation for
    a given number of iterations.'''
    for i in range(NumIterations + 1):
        plt.imshow(Grid, cmap = 'Greys', interpolation = 'nearest')
        plt.title('Round ' + str(i))
        plt.draw()
        plt.pause(.4)
        Grid = UpdateGrid(Grid, NewGrid)
    return

def main():
    '''Prompts the user for the size of the grid and how densely populated
    they want the grid to be at the starting iteration.'''

    NumRows = -1
    NumCols = -1
    ProbDensity = -1
    NumIterations = -1
    print('This appication will make a random simulation of Conway\'s Game of Life.')
    while type(NumRows) is not int or NumRows <= 0 or NumRows >= 100:
        NumRows = input('Enter the number of rows between 1 and 100: ')
    while type(NumCols) is not int or NumCols <= 0 or NumRows >= 100:
        NumCols = input('Enter the number of columns between 1 and 100: ')
    while type(ProbDensity) is not int or ProbDensity < 0 or ProbDensity >= 100:
        ProbDensity = input('Enter the probability density you want the pixels to be filled with as an integer between 0 and 100: ')
    while type(NumIterations) is not int or NumIterations <= 0 or NumIterations > 500:
        NumIterations = input('Enter the number of iterations as an integer between 1 and 500: ')

    Grid, DummyGrid = BuildGrid(NumRows, NumCols)
    for i in range(len(Grid)):
        for j in range(len(Grid[0])):
            RandNum = random.randrange(1,100)
            if RandNum <= ProbDensity:
                Grid[i][j] = 1
            else:
                Grid[i][j] = 0

    RunAutomata(Grid, DummyGrid, NumIterations)
    return



main()
