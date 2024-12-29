import pygame as pg

class Player:

    def __init__(self, screen): # Создание Объекта игрок
        self.angle = 90
        self.next_angle = 0
        self.alfa = 0
        self.win = screen
        self.x = 300
        self.y = 300
        self.rotate = False
        self.sur = pg.image.load('tank.png')
        self.sur = pg.transform.scale(self.sur, 
                                      (self.sur.get_width() / 8, self.sur.get_height() / 8))

    def move(self, keys): # Обработка нажатий движения для игрока
        if keys[pg.K_w]:
            self.y -= 5
            self.nex_angle = 90
            self.rotate = True
        elif keys[pg.K_s]:
            self.y += 5
            self.nex_angle = 270
            self.rotate = True
        elif keys[pg.K_a]:
            self.x -= 5
            self.nex_angle = 180
            self.rotate = True
        elif keys[pg.K_d]:
            self.x += 5
            self.nex_angle = 0
            self.rotate = True
        if self.rotate:
            self.alfa = self.next_angle - self.angle
            self.sur = pg.transform.rotate(self.sur, self.alfa)
            self.angle = self.next_angle
            self.rotate = False


    def draw(self): # Подготовка изображения для след кадра
        rect = self.sur.get_rect(center=(self.x, self.y))
        self.win.blit(self.sur, rect)

    def update(self):
        pass