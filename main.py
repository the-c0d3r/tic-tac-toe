from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.uix.button import Button
import random


class TicTacToe(App):

    def build(self):
        # Set the window's width and height
        Config.set('graphics', 'width', '700')
        Config.set('graphics', 'height', '500')

        self.title = "Tic Tac Toe"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def on_start(self):
        self.scoreboard = Record()
        self.resultbar = self.root.ids.result_label
        self.resultbar.text = self.scoreboard.get_result()
        self.statusbar = self.root.ids.status_label
        self.statusbar.text = "Game Start"
        self.create_button()

    def create_button(self):
        """ Creates the button """
        self.buttons = []
        for i in range(1,10):
            idnum = "btn"+str(i)
            btn = Button(text="", id=idnum, on_press=self.pressed_btn)
            self.root.ids.btn_box.add_widget(btn)
            self.buttons.append(btn)

    def wipe_button(self):
        """ Wipes all text in buttons """
        for btn in self.buttons:
            btn.text = ""

    def pressed_btn(self, btn):
        """ Handles the slot button press event """
        if btn.text == "":
            btn.text = "O"
            if self.checkwin("O"):
                #print("Player WIN")
                self.statusbar.text = "Player WIN"
                self.scoreboard.human += 1
                self.resultbar.text = self.scoreboard.get_result()
                return
            else:
                self.statusbar.text = "Player Moved. Computer turn"

            self.computer_turn()
            if self.checkwin("X"):
                #print("Computer WIN")
                self.statusbar.text = "Computer WIN"
                self.scoreboard.computer += 1
                self.resultbar.text = self.scoreboard.get_result()
                return
        else:
            self.statusbar.text = "That slot is already occupied"

    def pressed_playagain(self):
        """ Handles resetting of the playing field """
        self.wipe_button()
        # Resets the playing field
        self.statusbar.text = "Play Again"

    def pressed_exit(self):
        exit()

    def computer_turn(self):
        """
        Process computer's turn
        1. Check if there is possible win scenario for computer and execute
        2. Check if there is possible win scenario for Human and block
        3. If no scenario possible, then choose random
        """
        choices = self.get_empty_slot()
        if len(choices) != 0:
            for choice in choices:
                choice.text = "X"
                if self.checkwin("X"):
                    #print("Possible win scenario for computer")
                    self.statusbar.text = "Computer Moved. Player Turn"
                    return
                else:
                    choice.text = ""
            # if no possible win scenario, block human user
            for choice in choices:
                choice.text = "O"
                if self.checkwin("O"):
                    #print("Blocking possible win scenario for player")
                    choice.text = "X"
                    self.statusbar.text = "Computer Moved. Player Turn"
                    return
                else:
                    choice.text = ""

            # Means no possible win scenario for both computer and player
            random.choice(choices).text = "X"
        else:
            #print("Draw Match")
            self.statusbar.text = "Draw match for player and computer"
            self.scoreboard.draw += 1
            self.resultbar.text = self.scoreboard.get_result()

    def get_empty_slot(self):
        """ Returns the empty slot of tic tac toe """
        empty = []
        for btn in self.root.ids.btn_box.children:
            if btn.text == "":
                empty.append(btn)
        return empty

    def return_btn(self, string):
        """ Returns the button that have the id """
        for btn in self.buttons:
            if btn.id == string:
                return btn

    def checkwin(self, marker):
        s1 = self.return_btn('btn1').text
        s2 = self.return_btn('btn2').text
        s3 = self.return_btn('btn3').text
        s4 = self.return_btn('btn4').text
        s5 = self.return_btn('btn5').text
        s6 = self.return_btn('btn6').text
        s7 = self.return_btn('btn7').text
        s8 = self.return_btn('btn8').text
        s9 = self.return_btn('btn9').text

        return ((s1 == s2 == s3 == marker) or
                (s4 == s5 == s6 == marker) or
                (s7 == s8 == s9 == marker) or
                (s1 == s4 == s7 == marker) or
                (s2 == s5 == s8 == marker) or
                (s3 == s6 == s9 == marker) or
                (s1 == s5 == s9 == marker) or
                (s3 == s5 == s7 == marker))


class Record:
    """A small class for keeping track of scoreboard"""
    def __init__(self):
        self.human = 0
        self.computer = 0
        self.draw = 0

    def get_result(self):
        return str("Result: [{}] Computer, [{}] Player, [{}] Draw".format(self.computer, self.human, self.draw))


if __name__ == "__main__":
    TicTacToe().run()

