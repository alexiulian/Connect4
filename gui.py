import random

from guizero import App, Text, PushButton
from Service import service


class C4GameView:
    def __init__(self):
        self.player_status =-1
        self.ai_status = -1
        self.curent_player_color ="blue"
        self.game = service()
        self.app = App(title="Connect4", layout="grid")
        self.cells = []
        self.button0 = PushButton(self.app, command=self.on_click_0, grid=[0, 0])
        self.button1 = PushButton(self.app, command=self.on_click_1, grid=[1, 0])
        self.button2 = PushButton(self.app, command=self.on_click_2, grid=[2, 0])
        self.button3 = PushButton(self.app, command=self.on_click_3, grid=[3, 0])
        self.button4 = PushButton(self.app, command=self.on_click_4, grid=[4, 0])
        self.button5 = PushButton(self.app, command=self.on_click_5, grid=[5, 0])
        self.button6 = PushButton(self.app, command=self.on_click_6, grid=[6, 0])
        self.text = Text(self.app, text="Game on!", grid=[0, 7])
        self.status = 0
        self.winner = 0
        self.status_of_column0 = 5
        self.status_of_column1 = 5
        self.status_of_column2 = 5
        self.status_of_column3 = 5
        self.status_of_column4 = 5
        self.status_of_column5 = 5
        self.status_of_column6 = 5
        self.column = 0
        self.current_raw = -1
        self.current_column = -1
        self.winner_name = "Player"

    def get_all(self):
        return self.game.get_al()

    def display(self):
        for i in range(7):
            for j in range(6):
                text = Text(self.app, text="xxx", color="white", bg = "purple", grid=[i, j + 1])
                self.cells.append(text)
        # button0 = PushButton(self.app, command=self.on_clikc_7, grid=[0, 0])
        # self.button1 = PushButton(self.app, command=self.on_clikc_1, grid=[1, 0])
        # button2 = PushButton(self.app, command=self.on_clikc_2, grid=[2, 0])
        # button3 = PushButton(self.app, command=self.on_clikc_3, grid=[3, 0])
        # button4 = PushButton(self.app, command=self.on_clikc_4, grid=[4, 0])
        # button5 = PushButton(self.app, command=self.on_clikc_5, grid=[5, 0])
        # button6 = PushButton(self.app, command=self.on_clikc_6, grid=[6, 0])
        #self.text = Text(self.app, text="Game on going",grid=[0,7])
        self.app.display()


# intro = Text(app, text="Have a go with guizero and see what you can create.")

    def take_winner(self):
        self.winner = self.game.give_winner()

    def take_status(self):
        self.status = self.game.give_status()

    def block_button(self):
        button_number = self.game.return_blocking_button()
        #print("buton: ",button_number)
        if button_number == 0:
            self.button0.disable()
        elif button_number == 1:
            self.button1.disable()
        elif button_number == 2:
            self.button2.disable()
        elif button_number == 3:
            self.button3.disable()
        elif button_number == 4:
            self.button4.disable()
        elif button_number == 6:
            self.button6.disable()
        elif button_number == 5:
            self.button5.disable()

    def ai_move(self):
        for i in range(7):
            self.check_chioces_for_ui(i)
        self.ai_nr = self.verify()
        self.set()
        #print(self.ai_nr)

    def state_pos(self, i, j):
        # print("State called ",i,j)
        return self.game.state(i, j)
    def on_click(self,i):

        #print(i, self.crt_player)
        self.game.make_a_move(i,self.player_status)
        self.take_winner()
        self.take_status()
        self.block_button()
        if self.winner != 0:
            self.button0.disable()
            self.button1.disable()
            self.button2.disable()
            self.button3.disable()
            self.button4.disable()
            self.button5.disable()
            self.button6.disable()
            castigator = self.winner_name + " win!"
            self.text = Text(self.app, text=castigator, grid=[0, 7])
        else:
            self.checking_equality()
            self.ai_move()
            self.game.make_a_move(self.ai_nr, 1)
        self.take_winner()
        self.take_status()
        self.block_button()
        for i in range(42):
            row = i // 7
            column = i % 7
            status = self.game.state(row,column)
            cell_number_in_gui = 6 * column + row
            # print("State is ",st, lin, col)
            # print(i)

            if status == 0:
                self.cells[cell_number_in_gui].text_color = "white"
            elif status ==1:
                 self.cells[cell_number_in_gui].text_color = "orange"
                 self.cells[cell_number_in_gui].bg = "white"
                 self.cells[cell_number_in_gui].value = "xxx"
            else:
                #print("State is ", st, lin, col)
                #print(nr)
                self.cells[cell_number_in_gui].text_color = "yellow"
                self.cells[cell_number_in_gui].bg = "orange"
                self.cells[cell_number_in_gui].value = "yyy"





        if self.winner != 0:
            self.button0.disable()
            self.button1.disable()
            self.button2.disable()
            self.button3.disable()
            self.button4.disable()
            self.button5.disable()
            self.button6.disable()
            if self.winner == 1:
                self.winner_name = "PC"
            castigator =self.winner_name  + " win!!"
            self.text = Text(self.app, text=castigator, grid=[0, 7])
        else:
            self.checking_equality()

    def checking_equality(self):
        if self.game.check_equality():
            self.button0.disable()
            self.button1.disable()
            self.button2.disable()
            self.button3.disable()
            self.button4.disable()
            self.button5.disable()
            self.button6.disable()
            castigator = "Amazing draw!"
            self.text = Text(self.app, text=castigator, grid=[0, 7])

    def on_click_1(self):
        self.on_click(1)
    def on_click_2(self):
        self.on_click(2)
    def on_click_3(self):
        self.on_click(3)
    def on_click_4(self):
        self.on_click(4)
    def on_click_5(self):
        self.on_click(5)
    def on_click_6(self):
        self.on_click(6)
    def on_click_0(self):
        self.on_click(0)

    def set(self):
        self.current_raw = -1
        self.current_column = -1

    def get_column(self, i):
        if i == 0:
            return self.status_of_column0
        elif i == 1:
            return self.status_of_column1
        elif i == 2:
            return self.status_of_column2
        elif i == 3:
            return self.status_of_column3
        elif i == 4:
            return self.status_of_column4
        elif i == 5:
            return self.status_of_column5
        elif i == 6:
            return self.status_of_column6

    def check_chioces_for_ui(self, j):
        for i in reversed(range(6)):
            if j == 0:
                if self.game.state(i, j) == 0:
                    self.status_of_column0 = i
                    break
                if self.game.state(0, j) != 0:
                    self.status_of_column0 = -1
                    break
            if j == 1:
                if self.game.state(i, j) == 0:
                    self.status_of_column1 = i
                    break
                if self.game.state(0, j) != 0:
                    self.status_of_column1 = -1
                    break

            if j == 2:
                if self.game.state(i, j) == 0:
                    self.status_of_column2 = i
                    break
                if self.game.state(0, j) != 0:
                    self.status_of_column2 = -1
                    break

            if j == 3:
                if self.game.state(i, j) == 0:
                    self.status_of_column3 = i
                    break
                if self.game.state(0, j) != 0:
                    self.status_of_column3 = -1
                    break
            if j == 4:
                if self.game.state(i, j) == 0:
                    self.status_of_column4 = i
                    break
                if self.game.state(0, j) != 0:
                    self.status_of_column4 = -1
                    break
            if j == 5:
                if self.game.state(i, j) == 0:
                    self.status_of_column5 = i
                    break
                if self.game.state(0, j) != 0:
                    self.status_of_column5 = -1
                    break

            if j == 6:
                if self.game.state(i, j) == 0:
                    self.status_of_column6 = i
                    break
                if self.game.state(0, j) != 0:
                    self.status_of_column6 = -1
                    break

    def verify(self):
        ##return tru if clr had won
        #print(self.column0, self.column1, self.column2, self.column3, self.column4, self.column5, self.column6)
        #print(self.game.get_al())
        for i in range(6):
            for j in range(7):
                if j <= 3:
                    if self.game.state(i, j) == self.game.state(i, j + 1) and self.game.state(i,j) == self.game.state(i, j + 2) and self.game.state(i, j) == 1:
                        if j <= 5:
                            if self.get_column(j + 3) == i:
                                self.current_raw = i
                                self.col = j + 3
                                #print("h")
                                return self.current_column
                        if j >= 1:
                            if self.get_column(j - 1) == i:
                                self.current_raw = i
                                self.col = j + 3
                                # print("i")
                                return self.current_column

        for j in range(7):
            for i in range(6):
                if i <= 3:
                    if self.game.state(i, j) == self.game.state(i + 1, j) and self.game.state(i,j) == self.game.state(i + 2, j) and self.game.state(i, j) == 1:
                        if i - 1 >= 0:
                            if self.game.state(i - 1, j) == 0:
                                self.current_raw = i - 1
                                self.current_col = j
                                # print("j")
                                return self.current_column

        for i in range(6):
            for j in range(7):
                if j <= 3 and i <= 2:
                    if self.game.state(i, j) == self.game.state(i + 1, j + 1) and self.game.state(i,j) == self.game.state(i + 2, j + 2) and self.game.state(i, j) == 1:
                        if j >= 1 and i >= 1:
                            if self.get_column(j - 1) == i - 1:
                                self.current_raw = i - 1
                                self.current_col = j - 1
                                # print("k")
                                return self.current_column
                        if self.get_column(j + 3) == i + 3:
                            self.current_raw = i + 3
                            self.col = j + 3
                            # print("l")
                            return self.col

        for i in range(6):
            for j in range(7):
                if j >= 3 and i <= 2:
                    if self.game.state(i, j) == self.game.state(i + 1, j - 1) and self.game.state(i,j) == self.game.state(i + 2, j - 2)  and self.game.state(i, j) == 1:
                        if j <= 5:
                            if self.get_column(j + 1) == i - 1:
                                self.current_raw = i - 1
                                self.col = j + 1
                                # print("m")
                                return self.current_column
                        if self.get_column(j - 3) == i + 3:
                            self.current_raw = i + 3
                            self.current_column = j - 3
                            # print("n")
                            return self.current_column
        for i in range(6):
            for j in range(7):
                if j <= 3:
                    if self.game.state(i, j) == self.game.state(i,j + 1) and self.game.state(i, j) == self.game.state(i, j + 2) and self.game.state(i, j) == -1:
                        if j <= 5:
                            if self.get_column(j + 3) == i:
                                self.current_raw = i
                                self.current_column = j + 3
                                # print("a")
                                return self.current_column

                        if j >= 1:
                            if self.get_column(j - 1) == i:
                                self.current_raw = i
                                self.current_column = j - 1
                                # print("b")
                                return self.current_column
        for j in range(7):
            for i in range(6):
                if i <= 3:
                    if self.game.state(i, j) == self.game.state(i + 1, j) and self.game.state(i, j) == self.game.state(i + 2, j) and self.game.state(i, j) == -1:
                        if i - 1 >=0:
                            if self.game.state(i -1, j) == 0:
                                self.current_raw = i - 1
                                self.current_column = j
                                # print("c")
                                return self.current_column

        for i in range(6):
            for j in range(7):
                if j <= 3 and i <= 2:
                    if self.game.state(i, j) == self.game.state(i + 1, j + 1) and self.game.state(i,j) == self.game.state(i + 2, j + 2)  and self.game.state(i, j) == -1:
                        if j >= 1 and i >= 1:
                            if self.get_column(j-1) == i-1:
                                self.current_raw = i - 1
                                self.current_column = j - 1
                                # print("d")
                                return self.current_column
                        if self.get_column(j+3) == i+3:
                            self.current_raw = i+3
                            self.current_column = j+3
                            # print("e")
                            return self.current_column

        for i in range(6):
            for j in range(7):
                if j >= 3 and i <= 2:
                    if self.game.state(i, j) == self.game.state(i + 1, j - 1) and self.game.state(i,j) == self.game.state(i + 2, j - 2)  and self.game.state(i, j) == -1:
                       if j <= 5:
                           if self.get_column(j + 1) == i - 1:
                               self.current_raw = i - 1
                               self.current_column = j + 1
                               # print("f")
                               return self.current_column
                       if self.get_column(j - 3) == i + 3:
                           self.current_raw = i + 3
                           self.col = j - 3
                           # print("g")
                           return self.current_column

        for i in range(6):
            for j in range(7):
                if j <= 5:
                    if self.game.state(i, j) == self.game.state(i,j + 1)  and self.game.state(i, j) == -1:
                        if j <= 4:
                            if self.get_column(j + 2) == i:
                                self.current_raw = i
                                self.current_column = j + 2
                                # print("a1")
                                return self.current_column

                        if j >= 2:
                            if self.get_column(j - 1) == i:
                                self.current_raw = i
                                self.current_column = j - 1
                                # print("b1")
                                return self.current_column
        for j in range(7):
            for i in range(6):
                if i <= 4:
                    if self.game.state(i, j) == self.game.state(i + 1, j)  and self.game.state(i, j) == -1:
                        if i - 1 >=0:
                            if self.game.state(i -1, j) == 0:
                                self.current_raw = i - 1
                                self.current_column = j
                                # print("c1")
                                return self.current_column

        for i in range(6):
            for j in range(7):
                if j <= 4 and i <= 3:
                    if self.game.state(i, j) == self.game.state(i + 1, j + 1)  and self.game.state(i, j) == -1:
                        if j >= 1 and i >= 1:
                            if self.get_column(j-1) == i-1:
                                self.current_raw = i - 1
                                self.current_column = j - 1
                                # print("d1")
                                return self.current_column
                        if self.get_column(j+2) == i+2:
                            self.current_raw = i+2
                            self.current_column = j+2
                            # print("e1")
                            return self.current_column

        for i in range(6):
            for j in range(7):
                if j >= 2 and i <= 3:
                    if self.game.state(i, j) == self.game.state(i + 1, j - 1)  and self.game.state(i, j) == -1:
                       if j <= 5:
                           if self.get_column(j + 1) == i - 1:
                               self.current_raw = i - 1
                               self.current_column = j + 1
                               # print("f")
                               return self.current_column
                       if self.get_column(j - 2) == i + 2:
                           self.current_raw = i + 2
                           self.current_column = j - 2
                           # print("g1")
                           return self.current_column
        for i in range(6):
            for j in range(7):
                if j <= 5:
                    if self.game.state(i, j) == self.game.state(i,j + 1)  and self.game.state(i, j) == 1:
                        if j <= 4:
                            if self.get_column(j + 2) == i:
                                self.current_raw = i
                                self.current_column = j + 2
                                # print("a1")
                                return self.current_column

                        if j >= 2:
                            if self.get_column(j - 1) == i:
                                self.current_raw = i
                                self.current_column = j - 1
                                # print("b1")
                                return self.current_column
        for j in range(7):
            for i in range(6):
                if i <= 4:
                    if self.game.state(i, j) == self.game.state(i + 1, j)  and self.game.state(i, j) == 1:
                        if i - 1 >=0:
                            if self.game.state(i -1, j) == 0:
                                self.current_raw = i - 1
                                self.current_col = j
                                # print("c1")
                                return self.current_column

        for i in range(6):
            for j in range(7):
                if j <= 4 and i <= 3:
                    if self.game.state(i, j) == self.game.state(i + 1, j + 1)  and self.game.state(i, j) == 1:
                        if j >= 1 and i >= 1:
                            if self.get_column(j-1) == i-1:
                                self.current_raw = i - 1
                                self.current_column = j - 1
                                # print("d1")
                                return self.current_column
                        if self.get_column(j+2) == i+2:
                            self.current_raw = i+2
                            self.current_column = j+2
                            # print("e1")
                            return self.current_column

        for i in range(6):
            for j in range(7):
                if j >= 2 and i <= 3:
                    if self.game.state(i, j) == self.game.state(i + 1, j - 1)  and self.game.state(i, j) == 1:
                       if j <= 5:
                           if self.get_column(j + 1) == i - 1:
                               self.current_raw = i - 1
                               self.current_column = j + 1
                               # print("f")
                               return self.current_column
                       if self.get_column(j - 2) == i + 2:
                           self.current_raw = i + 2
                           self.current_col = j - 2
                           # print("g1")
                           return self.current_column

        while True:
            j = random.randint(0,6)
            if self.get_column(j) != -1:
                self.current_column = j
                # print("random")
                return self.current_column

    def state(self):
        return self.game.state



