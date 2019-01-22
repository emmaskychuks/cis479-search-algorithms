from objects.node import Node

class Map:
    def __init__(self, height, width):
        # Make a 8 x 11 matrix
        self.height = height
        self.width = width

        self.matrix = [[Node(x, y) for y in range(width)] for x in range(height)]

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
            return True
        else:
            return False

    def print(self):
        for row in self.matrix:
            print([node.value for node in row])