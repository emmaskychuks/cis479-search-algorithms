from objects.map import Map
from objects.node import Node
from algorithms.breadthFirstSearch import breadthFirstSearch
from algorithms.uniformCostSearch import uniformCostSearch
from algorithms.depthFirstSearch import depthFirstSearch

def main():
    map = Map(8, 11)

    intitialNode = Node(4, 5)
    goalNode = Node(0, 10)
    
    #print("Breadth First Search")
    #result = breadthFirstSearch(map, intitialNode, goalNode)
    #result.print()

    #print("Uniform Cost Search")
    #result = uniformCostSearch(map, intitialNode, goalNode)
    #result.print()

    print("Depth First Search")
    result = depthFirstSearch(map, intitialNode, goalNode)
    result.print()

if __name__ == "__main__":
    main()