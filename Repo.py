class repo:
    def __init__(self):
        self.matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

    def states(self, row, column):
        return self.matrix[row][column]
    def update_color(self, row, column, color):
        self.matrix[row][column] = color
    def getall(self):
        return self.matrix