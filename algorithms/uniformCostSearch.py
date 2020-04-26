from queue import PriorityQueue
from objects.node import Node

def uniformCostSearch(grid, initialNode, goalNode):

    frontier = PriorityQueue()

    grid.matrix[initialNode.x][initialNode.y].visited = True
    grid.matrix[initialNode.x][initialNode.y].value = "00"
    grid.matrix[initialNode.x][initialNode.y].cost = 0

    startNode = grid.matrix[initialNode.x][initialNode.y]

    frontier.put(tuple([startNode.cost, 0, startNode]))

    return uniformCostSearchHelper(frontier, grid, initialNode, goalNode, 1)

def uniformCostSearchHelper(frontier, grid, startNode, goalNode, orderNumber):
    
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
                frontier.put(tuple([successorNode.cost, orderNumber, successorNode]))
                orderNumber += 1


        #check north
        if(grid.isWithinBoundary(Node(currentNode.x - 1, currentNode.y)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x - 1][currentNode.y]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = currentNode.cost + 1
                frontier.put(tuple([successorNode.cost, orderNumber, successorNode]))
                orderNumber += 1
                
        #check east
        if(grid.isWithinBoundary(Node(currentNode.x, currentNode.y + 1)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x][currentNode.y + 1]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = currentNode.cost + 2
                frontier.put(tuple([successorNode.cost, orderNumber, successorNode]))
                orderNumber += 1

        #check south
        if(grid.isWithinBoundary(Node(currentNode.x + 1, currentNode.y)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x + 1][currentNode.y]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                successorNode.cost = currentNode.cost + 3
                frontier.put(tuple([successorNode.cost, orderNumber, successorNode]))
                orderNumber += 1

    return uniformCostSearchHelper(frontier, grid, startNode, goalNode, orderNumber)