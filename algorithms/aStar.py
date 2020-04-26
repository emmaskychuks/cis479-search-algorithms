from queue import PriorityQueue
from objects.node import Node

def aStarSearch(grid, initialNode, goalNode):

    frontier = PriorityQueue()

    grid.matrix[initialNode.x][initialNode.y].visited = True
    grid.matrix[initialNode.x][initialNode.y].value = "00"
    grid.matrix[initialNode.x][initialNode.y].cost = 0
    grid.matrix[initialNode.x][initialNode.y].aStarCost = grid.distance(initialNode, goalNode)

    startNode = grid.matrix[initialNode.x][initialNode.y]

    frontier.put(tuple([startNode.aStarCost, 0, startNode]))

    return aStarSearchHelper(frontier, grid, initialNode, goalNode, 1)

def aStarSearchHelper(frontier, grid, startNode, goalNode, orderNumber):
    
    if(frontier.empty() or grid.matrix[goalNode.x][goalNode.y].visited == True):
        return grid

    else:    
        tupleItem = frontier.get()
        currentNode = tupleItem[2]

        #check west
        if(grid.isWithinBoundary(Node(currentNode.x, currentNode.y - 1))and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x][currentNode.y - 1]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = currentNode.cost + 2
                successorNode.aStarCost = successorNode.cost + grid.distance(successorNode, goalNode)
                frontier.put(tuple([successorNode.aStarCost, orderNumber, successorNode]))
                orderNumber += 1


        #check north
        if(grid.isWithinBoundary(Node(currentNode.x - 1, currentNode.y)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x - 1][currentNode.y]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = currentNode.cost + 1
                successorNode.aStarCost = successorNode.cost + grid.distance(successorNode, goalNode)
                frontier.put(tuple([successorNode.aStarCost, orderNumber, successorNode]))
                orderNumber += 1
                
        #check east
        if(grid.isWithinBoundary(Node(currentNode.x, currentNode.y + 1)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x][currentNode.y + 1]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = currentNode.cost + 2
                successorNode.aStarCost = successorNode.cost + grid.distance(successorNode, goalNode)
                frontier.put(tuple([successorNode.aStarCost, orderNumber, successorNode]))
                orderNumber += 1

        #check south
        if(grid.isWithinBoundary(Node(currentNode.x + 1, currentNode.y)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x + 1][currentNode.y]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = currentNode.cost + 3
                successorNode.aStarCost = successorNode.cost + grid.distance(successorNode, goalNode)
                frontier.put(tuple([successorNode.aStarCost, orderNumber, successorNode]))
                orderNumber += 1

    return aStarSearchHelper(frontier, grid, startNode, goalNode, orderNumber)