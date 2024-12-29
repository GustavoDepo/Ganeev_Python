import pygame as pg
from player_tank import Player
from map import Map

class Game:

    def __init__(self): # Создание объекта Игра
        pg.init()
        self.win = pg.display.set_mode((600, 600))
        self.player = Player(self.win)
        self.clock = pg.time.Clock()
        self.map = Map(self.win)

    def game(self):
        while True:
            self.move()
            self.draw()
            self.update()


    def move(self): # Обработка нажатия для Игры
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        self.player.move(pg.key.get_pressed())
        

    def draw(self): # Подгатовка изо для след кадра
        self.win.fill('white')
        self.map.drow()
        self.player.draw()

    def update(self): # Обновление картинки
        self.clock.tick(60)
        pg.display.update()

Game().game()