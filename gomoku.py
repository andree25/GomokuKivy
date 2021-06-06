from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import (ListProperty, NumericProperty)
from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label


class GridEntry(Button):
    coords = ListProperty([0, 0])


class TicTacToeGrid(GridLayout):
    status = ListProperty([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    current_player = NumericProperty(1)

    def __init__(self, *args, **kwargs):
        super(TicTacToeGrid, self).__init__(*args, **kwargs)

        for row in range(21):
            for column in range(21):
                grid_entry = GridEntry(coords=(row, column))
                grid_entry.bind(on_release=self.button_pressed)
                self.add_widget(grid_entry)

    def button_pressed(self, button):
        print('{} button clicked!'.format(button.coords))
        player = {1: 'O', -1: 'X'}
        colours = {1: (1, 0, 0, 1), -1: (0, 1, 0, 1)}
        row, column = button.coords

        status_index = 21 * row + column
        already_played = self.status[status_index]

        if not already_played:
            self.status[status_index] = self.current_player
            button.text = {1: 'O', -1: 'X'}[self.current_player]
            button.background_color = colours[self.current_player]
            self.current_player *= -1

    def on_status(self, instance, new_value):
        status = new_value

        sums = [sum(status[0:21]), sum(status[21:42]), sum(status[42:63]), sum(status[63:84]), sum(status[84:105]),
                sum(status[105:126]), sum(status[126:147]), sum(status[147:168]),
                sum(status[168:189]), sum(status[189:210]), sum(status[210:231]), sum(status[231:252]),
                sum(status[252:273]), sum(status[273:294]), sum(status[294:315]),
                sum(status[315:336]), sum(status[336:357]), sum(status[357:378]), sum(status[378:399]),
                sum(status[399:420]), sum(status[420:441]),
                sum(status[0::21]), sum(status[1::21]), sum(status[2::21]), sum(status[3::21]), sum(status[4::21]),
                sum(status[5::21]), sum(status[6::21]), sum(status[7:21]), sum(status[8::21]), sum(status[9::21]),
                sum(status[10::21]), sum(status[11::21]), sum(status[12::21]), sum(status[13::21]), sum(status[14::21]),
                sum(status[15::21]), sum(status[16::21]), sum(status[17::21]), sum(status[18::21]), sum(status[19::21]),
                sum(status[20::21]), sum(status[21::21]),
                sum(status[1:-1:20]), sum(status[2:-2:20]), sum(status[3:-3:20]), sum(status[4:-4:20]),
                sum(status[5:-5:20]), sum(status[6:-6:20]),
                sum(status[7:-7:20]), sum(status[8:-8:20]), sum(status[9:-9:20]), sum(status[10:-10:20]),
                sum(status[11:-11:20]), sum(status[12:-12:20]), sum(status[13:-13:20]), sum(status[14:-14:20]),
                sum(status[15:-15:20]), sum(status[16:-16:20]),
                sum(status[17:-17:20]), sum(status[18:-18:20]), sum(status[19:-19:20]), sum(status[20:-20:20]),
                sum(status[::22]), sum(status[1::22]), sum(status[2::22]), sum(status[3::22]), sum(status[4::22]),
                sum(status[5::22]), sum(status[6::22]), sum(status[7::22]),
                sum(status[8::22]), sum(status[9::22]), sum(status[10::22]), sum(status[11::22]), sum(status[12::22]),
                sum(status[13:22]), sum(status[14::22]), sum(status[15::22]),
                sum(status[15::22]), sum(status[17::22]), sum(status[18::22]), sum(status[19::22]), sum(status[20::22]),
                sum(status[21::22])]

        winner = None
        if 5 in sums:
            winner = "O wins!"
        elif -5 in sums:
            winner = "X wins!"
        elif 0 not in self.status:
            winner = "Draw!"

        if winner:
            popup = ModalView(size_hint=(0.75, 0.5))
            victory_label = Label(text=winner, font_size=50)
            popup.add_widget(victory_label)
            popup.bind(on_dismiss=self.reset)
            popup.open()
        print(winner)

    def reset(self, *args):
        self.status = [0 for _ in range(441)]

        for child in self.children:
            child.text = ''
            child.background_color = (1, 1, 1, 1)

        self.current_player = -1


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()


if __name__ == "__main__":
    TicTacToeApp().run()
