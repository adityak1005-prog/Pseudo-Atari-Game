import pygame
from env import Environment
from renderer import Renderer
import numpy as np


class Game:
    def __init__(self):
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.env=Environment()
        self.renderer = Renderer(self.env)
        self.action = np.zeros(2, int)
        self.counter = 0
        self.reward = 0


    def step(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and not self.game_over:
                self.counter += 1
                if event.key == pygame.K_UP:
                    self.action = np.array([-1, 0])
                if event.key == pygame.K_DOWN:
                    self.action = np.array([1, 0])
                if event.key == pygame.K_LEFT:
                    self.action = np.array([0, -1])
                if event.key == pygame.K_RIGHT:
                    self.action = np.array([0, 1])
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_over = True
        self.reward = self.env.reward(self.action, self.counter)
        self.action[:] = 0
        self.renderer.render_bg(self.counter)
        if np.array_equal(self.env.sprite, self.env.target):
            self.game_over = 1
        self.clock.tick(60)

if __name__ == '__main__':
    game = Game() 
    while not game.game_over:
        game.step()