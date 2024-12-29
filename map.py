import pygame as pg

class Map:

    def __init__(self, win):
        self.win = win
        self.points = [[1] * 20 for i in range(20)]
        self.block = pg.image.load('block.jpg')

    def drow(self):
        for i in range(len(self.points)):
            for j in range(len(self.points[i])):
                if self.points[i][j] == 1:
                    self.drow_block(i, j)
        print()

    def drow_block(self, i, j):
        rect = self.block.get_rect(center=(i * 30 + 15, j * 30 + 15))
        print(i * 30 + 15, j * 30 + 15)
        self.win.blit(self.block, rect)


