import math
import tkinter as tk
from tkinter import messagebox
import pygame

class gol(object):
    cells = []
    w = 500
    rows = 20

    def __init__(self, color):
        self.color = color
    def addcell(self, x, y):
        self.cells.append([x, y])
    def drawcells(self, surface):
        dis = self.w // self.rows
        for i in range(len(self.cells)):
            pygame.draw.rect(surface, (0, 255, 0), (self.cells[i][0] * dis + 1, self.cells[i][1] * dis + 1, dis - 2, dis - 2))

class cell(object):
    rows = 20
    w = 500
    color = (0, 255, 0)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self, surface):
        dis = self.w // self.rows
        pygame.draw.rect(surface, self.color, (self.x*dis+1, self.y*dis+1, dis-2, dis-2))


def create(w, ):
    #a =
    #for i in range(w):

    return 1

def draw(w, rows, surface,data):
    btw = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + btw
        y = y + btw
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))
    data.drawcells(surface)

def redraw(w, rows, surface, data):
    surface.fill((0,0,0))
    draw(w, rows, surface, data)
    pygame.display.update()


def find8(data, x, y):
    ring = [[],[],[],[],[],[],[],[]]
    cols = 20
    rows = 20
    #topleft
    if x == 0 and y == 0:
        ring[0] = [19,19]
    elif x == 0:
        ring[0] = [19, y-1]
    elif y == 0:
        ring[0] = [x-1, 19]
    else:
        ring[0] = [x-1, y-1]
    #top
    if y == 0:
        ring[1] = [x, 19]
    else:
        ring[1] = [x, y-1]

    #topright
    if x == 19 and y == (0):
        ring[2] = [0,  19]
    elif x == 19:
        ring[2] = [0, y-1]
    elif y == 0:
        ring[2] = [x+1, 19]
    else:
        ring[2] = [x+1, y-1]
    #right

def main():
    width = 500
    rows = 20
    surface = pygame.display.set_mode((width,width))
    flag = True
    clock = pygame.time.Clock()
    data = gol((255, 255, 255))
    data.addcell(0, 1)
    data.addcell(2, 2)
    data.addcell(3, 3)



    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        redraw(width, rows, surface, data)

main()


