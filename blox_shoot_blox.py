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

class Bullet(Image):
    def __init__(self, spaceship, **kwargs):
        super(Bullet, self).__init__(**kwargs)
        self.source = 'C://Users//TUF RTX 4060//Desktop//Project//bullet.jpg'
        self.pos_hint = {'center_x': spaceship.center_x, 'center_y': spaceship.top}
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, *args):
        self.y += 10
        if self.top > Window.height:
            self.parent.remove_widget(self)


class Enemy(Image):
    def __init__(self, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        self.source = 'C://Users//TUF RTX 4060//Desktop//Project//moster.png'
        self.pos = (randint(0, Window.width - self.width), Window.height)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, *args):
        self.y -= 5
        if self.top < 0:
            self.pos = (randint(0, Window.width - self.width), Window.height)


class SpaceGame(Widget):
    def __init__(self, **kwargs):
        super(SpaceGame, self).__init__(**kwargs)
        self.spaceship = SpaceShip()
        self.add_widget(self.spaceship)
        self.bullets = []
        self.enemies = []

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, *args):
        self.check_collision()
        self.move_enemies()
        for bullet in self.bullets:
            bullet.update()

    def check_collision(self):
        for enemy in self.enemies:
            if self.spaceship.collide_widget(enemy):
                self.remove_widget(self.spaceship)
                game_over_label = Label(text='Game Over', font_size=70, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                self.add_widget(game_over_label)
                return

            for bullet in self.bullets:
                if bullet.collide_widget(enemy):
                    self.remove_widget(bullet)
                    self.remove_widget(enemy)
                    self.enemies.remove(enemy)
    def move_enemies(self):
        if randint(1, 50) == 1:
            enemy = Enemy()
            self.enemies.append(enemy)
            self.add_widget(enemy)

    def on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            self.spaceship.move('up')
        elif keycode[1] == 's':
            self.spaceship.move('down')
        elif keycode[1] == 'd':
            self.spaceship.move('right')
        elif keycode[1] == 'a':
            self.spaceship.move('left')
        elif keycode[1] == 'spacebar':
            bullet = Bullet(self.spaceship)
            self.bullets.append(bullet)
            self.add_widget(bullet)
