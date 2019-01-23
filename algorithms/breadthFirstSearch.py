from collections import deque
from objects.node import Node

def breadthFirstSearch(grid, intitialNode, goalNode):
    frontier = deque()

    grid.matrix[intitialNode.x][intitialNode.y].visited = True
    grid.matrix[intitialNode.x][intitialNode.y].value = "00"
    startNode = grid.matrix[intitialNode.x][intitialNode.y]

    frontier.append(startNode)

    return breadthFirstSearchHelper(frontier, grid, intitialNode, goalNode, 1)


def breadthFirstSearchHelper(frontier, grid, startNode, goalNode, orderNumber):

    if(len(frontier) == 0 or grid.matrix[goalNode.x][goalNode.y].visited == True):
        return grid

    else:    
        currentNode = frontier.popleft()
        #check north
        if(grid.isWithinBoundary(Node(currentNode.x - 1, currentNode.y)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x - 1][currentNode.y]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                frontier.append(successorNode)
                orderNumber += 1
        #check west
        if(grid.isWithinBoundary(Node(currentNode.x, currentNode.y - 1)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x][currentNode.y - 1]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                frontier.append(successorNode)
                orderNumber += 1
        #check east
        if(grid.isWithinBoundary(Node(currentNode.x, currentNode.y + 1)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x][currentNode.y + 1]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                frontier.append(successorNode)
                orderNumber += 1

        #check south
        if(grid.isWithinBoundary(Node(currentNode.x + 1, currentNode.y)) and grid.matrix[goalNode.x][goalNode.y].visited != True):
            successorNode = grid.matrix[currentNode.x + 1][currentNode.y]
            if successorNode.visited != True:
                successorNode.value = str("%02d" % orderNumber)
                successorNode.visited = True
                frontier.append(successorNode)
                orderNumber += 1

    return breadthFirstSearchHelper(frontier, grid, startNode, goalNode, orderNumber)

