from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import StringProperty


class TicTacToe(App):
    statusbar = StringProperty()

    def build(self):
        Config.set('graphics', 'width', '700')
        Config.set('graphics', 'height', '500')

        self.title = "Tic Tac Toe"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def on_start(self):
        self.statusbar = "Game Start"

    def pressed_btn(self):
        print("Button pressed")

if __name__ == "__main__":
    TicTacToe().run()

