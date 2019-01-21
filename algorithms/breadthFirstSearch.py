from collections import deque
from node import Node

def breadthFirstSearch(grid, intitialNode, goalNode):
    pass
    exploredSet = set()
    frontier = deque()

    breadthFirstSearchHelper(exploredSet, frontier, grid, intitialNode, goalNode, 00)


def breadthFirstSearchHelper(exploredSet, frontier, grid, startNode, goalNode, orderNumber):

    frontier.append(Node(startNode.x, startNode.y))

    if(frontier == [] or goalNode.visited == True):
        return
    else:
        currentNode = frontier.popleft()
        #check north
        successorNode = Node(currentNode.x+1, currentNode.y)
        if(grid.isWithinBoundary(successorNode)):
            if successorNode.visited != True:
                frontier.append(successorNode)
                successorNode.value = str(++orderNumber)


        #check west

        #check east

        #check south
