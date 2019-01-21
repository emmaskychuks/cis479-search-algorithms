from node import Node

class Map:
    def __init__(self, width, height):
        # Make a 8 x 11 matrix
        self.matrix = [[Node(x, y) for x in range(height)] for y in range(width)]

        #Setting up obstacles in map
        # 0,0 is top left
        self.matrix[4][3].visited = True
        self.matrix[4][3].value = "##"

        self.matrix[4][4].visited = True
        self.matrix[4][4].value = "##"

        self.matrix[3][4].visited = True
        self.matrix[3][4].value = "##"

        self.matrix[2][4].visited = True
        self.matrix[2][4].value = "##"

        self.matrix[5][6].visited = True
        self.matrix[5][6].value = "##"

        self.matrix[5][7].visited = True
        self.matrix[5][7].value = "##"

        self.matrix[2][5].visited = True
        self.matrix[2][5].value = "##"

        self.matrix[2][6].visited = True
        self.matrix[2][6].value = "##"

        self.matrix[2][7].visited = True
        self.matrix[2][7].value = "##"

        self.matrix[4][7].visited = True
        self.matrix[4][7].value = "##"

        self.matrix[3][7].visited = True
        self.matrix[3][7].value = "##"

        self.matrix[2][7].visited = True
        self.matrix[2][7].value = "##"

    def isWithinBoundary(self, node):
        # Check if a node is within the boundary of the map
        if (node.x >= 0 and node.x < 8) and (node.y >= 0 and node.y < 11):
            return False
        else:
            return True

    def print(self):
        for x in self.matrix:
            print([node.value for node in x])
            
