class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.value = "[]"
        self.cost = 0
        self.aStarCost = 0

    def __lt__(self, other):
        return self.aStarCost < other.aStarCost
    