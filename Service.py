from threading import Condition
from Repo import *

class service:
    def __init__(self):
        # self.matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.repo_of_connect4 = repo()
        self.status = 0
        self.winner = 0
        self.blocking_button = 7
    def make_a_move(self, column, color):
        for i in reversed(range(6)):
            #print(i,colm, self.matrix[i][colm])
            if self.repo_of_connect4.states(i, column) == 0:
                self.repo_of_connect4.update_color(i, column, color)
                #print("color ", self.repo_of_c4.states(i,colm))
                #self.matrix[i][colm] = clr
                #print("Changed", i, colm)
                if i == 0:
                    self.blocking_button = column
                    self.return_blocking_button()
                break
        if self.verify(color):
            status = 1
            winner = color
            self.set_status(status)
            self.set_winner(winner)
            #print(i,colm)

    def give_matrix(self):
        self.repo_of_connect4.getall()
    def return_blocking_button(self):
        return self.blocking_button

    def check_equality(self):
        for i in range(6):
            for j in range(7):
                if self.repo_of_connect4.states(i,j) == 0:
                    return False
        return True
    def set_status(self,status):
        self.status = status
    def give_status(self):
        return self.status

    def set_winner(self, winner):
        self.winner = winner
    def give_winner(self):
        pass
        return self.winner
    def verify(self, color):
        ##return tru if clr had won
        for i in range(6):
            for j in range(7):
                if j <= 3:
                    if self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i,j + 1) and self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i,j+2) and self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i,j + 3) and self.repo_of_connect4.states(i,j) == color:
                        # print("abc",i,j,self.matrix[i][j],self.matrix[i][j+3])
                        # print("a", i,j)
                        return True


        for j in range(7):
            for i in range(6):
                if i <= 2:
                    if self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i + 1,j) and self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i + 2,j) and self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i + 3,j) and self.repo_of_connect4.states(i,j) == color:
                        # print("b", i,j)
                        return True

        for i in range(6):
            for j in range(7):
                if j <= 3 and i <= 2:
                    if self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i + 1,j + 1) and self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i + 2,j + 2) and self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i + 3,j + 3) and self.repo_of_connect4.states(i,j) == color:
                        # print("c", i,j)
                        return True

        for i in range(6):
            for j in range(7):
                if j >= 3 and i <= 2:
                    if self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i + 1,j -1) and self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i + 2,j - 2) and self.repo_of_connect4.states(i,j) == self.repo_of_connect4.states(i + 3,j - 3) and self.repo_of_connect4.states(i,j) == color:
                        # print("d", i,j)
                        return True
        return False
    def state(self,row,column):
        # print("State called ",i,j)
        return self.repo_of_connect4.states(row,column)
    def get_al(self):
        return self.repo_of_connect4.getall()

