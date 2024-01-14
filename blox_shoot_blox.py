from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
from random import randint
from kivy.clock import Clock

class SpaceShip(Widget):
    def __init__(self, **kwargs):
        super(SpaceShip, self).__init__(**kwargs)
        self.image = Image(source='C://Users//TUF RTX 4060//Desktop//Project//—Pngtree—cartoon airplane model_2652515.png')
        self.add_widget(self.image)

    def move(self, direction):
        if direction == 'up' and self.y < Window.height - 100:
            self.y += 10
        elif direction == 'down' and self.y > 0:
            self.y -= 10
        elif direction == 'right' and self.x < Window.width - 100:
            self.x += 10
        elif direction == 'left' and self.x > 0:
            self.x -= 10