import pygame as pg
import sys
import random
from pygame.locals import *

size = width, height = 800, 600
border_size = 10
color = 180, 212, 101
black = pg.Color(0, 0, 0)

def rand_color():
    return random.randint(0, 255), random.randint(0, 255),
random.randint(0, 255)

def random_position():
    return random.randint(50, 750), random.randint(50, 550)

def create_border(game_surface):
    for i in range(height):
        pg.draw.rect(game_surface, (99, 136, 64), (0, i, 25, 25), 0)
        pg.draw.rect(game_surface, (99, 136, 64), (width - 25, i, 25, 25), 0)
    for i in range(width):
        pg.draw.rect(game_surface, (99, 136, 64), (i, 0, 25, 25), 0)
        pg.draw.rect(game_surface, (99, 136, 64), (i, height - 25, 25, 25), 0)

class Food(object):
    def __init__(self, x_pos_food = None, y_pos_food = None, food_color = None):
        if x_pos_food is None:
            x_pos_food, y_pos_food = random_position()
            food_color = (215, 54, 48)
        self.x_pos_food, self.y_pos_food, self.color = x_pos_food,y_pos_food, food_color
        self.food_pos = [self.x_pos_food, self.y_pos_food]

    def is_eaten(self, x, y):
        if x == self.x_pos_food and y == self.y_pos_food:
            self.x_pos_food, self.y_pos_food = random_position()

    def draw_food(self, game_surface):
        pg.draw.rect(game_surface, self.color, (self.x_pos_food,
self.y_pos_food, 25, 25), 0)

class Controls():
    def event_loop(self, turn):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT or event.key == ord('d'):
                    turn = "RIGHT"
                elif event.key == pg.K_LEFT or event.key == ord('a'):
                    turn = "LEFT"
                elif event.key == pg.K_UP or event.key == ord('w'):
                    turn = "UP"
                elif event.key == pg.K_DOWN or event.key == ord('s'):
                    turn = "DOWN"
        return turn

class Snake():
    def __init__(self, s_color):
        self.head = [150, 50]
        self.body = [[150, 50], [140, 50], [130, 50]]
        self.s_color = s_color
        self.s_direction = "RIGHT"
        self.turn = "RIGHT"
    def direcrion(self):
        if self.turn == "RIGHT" and self.turn != "LEFT":
            self.s_direction = self.turn
        if self.turn == "LEFT" and self.turn != "RIGHT":
            self.s_direction = self.turn
        if self.turn == "UP" and self.turn != "DOWN":
            self.s_direction = self.turn
        if self.turn == "DOWN" and self.turn != "UP":
            self.s_direction = self.turn
    def turn_head(self):
        if self.s_direction == "RIGHT":
            self.head[0] += 10
            self.head[0] -= 10
            self.head[1] += 10
            self.head[1] -= 10
    def mechanics(self, food, x, y):
        self.body.insert(0, list(self.head))

        if self.head[0] == food[0] and self.head[1] == food[1]:
            if x == self.x_pos_food and y == self.y_pos_food:
                self.x_pos_food, self.y_pos_food = random_position()
        else:
            self.body.pop()
    def draw_snake(self, screen):
        for pos in self.body:
            pg.draw.rect(screen, self.s_color, (pos[0], pos[1], 10, 10), 0)
    def crush(self, size):
        for segment in self.body[1:]:
            if segment[0] == self.head[0] and segment[1] == self.head[1]:
                pg.quit()