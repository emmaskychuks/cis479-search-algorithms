from queue import PriorityQueue
from objects.node import Node

def greedySearch(grid, intitialNode, goalNode):

    frontier = PriorityQueue()

    grid.matrix[intitialNode.x][intitialNode.y].visited = True
    grid.matrix[intitialNode.x][intitialNode.y].value = "00"
    grid.matrix[intitialNode.x][intitialNode.y].cost = 0

    startNode = grid.matrix[intitialNode.x][intitialNode.y]

    frontier.put(tuple([startNode.cost, startNode]))

    return greedySearchHelper(frontier, grid, intitialNode, goalNode, 1)

def greedySearchHelper(frontier, grid, startNode, goalNode, orderNumber):
    
    if(frontier.empty() or grid.matrix[goalNode.x][goalNode.y].visited == True):
        return grid

    else:    
        tupleItem = frontier.get()
        currentNode = tupleItem[1]

        #check west
        if(grid.isWithinBoundary(Node(currentNode.x, currentNode.y - 1))and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x][currentNode.y - 1]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = grid.distance(successorNode, goalNode)
                frontier.put(tuple([successorNode.cost + currentNode.cost, successorNode]))
                orderNumber += 1


        #check north
        if(grid.isWithinBoundary(Node(currentNode.x - 1, currentNode.y)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x - 1][currentNode.y]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = grid.distance(successorNode, goalNode)
                frontier.put(tuple([successorNode.cost + currentNode.cost, successorNode]))
                orderNumber += 1
                
        #check east
        if(grid.isWithinBoundary(Node(currentNode.x, currentNode.y + 1)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x][currentNode.y + 1]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = grid.distance(successorNode, goalNode)
                frontier.put(tuple([successorNode.cost + currentNode.cost, successorNode]))
                orderNumber += 1

        #check south
        if(grid.isWithinBoundary(Node(currentNode.x + 1, currentNode.y)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x + 1][currentNode.y]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = grid.distance(successorNode, goalNode)
                frontier.put(tuple([successorNode.cost + currentNode.cost, successorNode]))
                orderNumber += 1

    return greedySearchHelper(frontier, grid, startNode, goalNode, orderNumber)