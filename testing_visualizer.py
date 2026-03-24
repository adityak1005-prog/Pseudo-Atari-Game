import time
from agent import Agent
import numpy as np
import pygame
from game import Game

Q_stored = np.zeros((4, 10, 10))

class Testing:
    def __init__(self):
        self.agent = Agent(epsilon=0.2)

    def learn(self):
        self.agent.QL(50)

    def test(self, Q_stored):
        self.agent.game = Game()
        self.agent.get_state()
        # old_state = state
        greedy = np.argmax(Q_stored, axis=0)
        while not self.agent.game.game_over:
            match greedy[self.agent.state[0]][self.agent.state[1]]:
                case 0:
                    keydown = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
                    pygame.event.post(keydown)
                case 1:
                    keydown = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
                    pygame.event.post(keydown)
                case 2:
                    keydown = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
                    pygame.event.post(keydown)
                case 3:
                    keydown = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
                    pygame.event.post(keydown)
            self.agent.game.step()
            self.agent.get_state()
            time.sleep(0.5)

if __name__ == '__main__':
    testing = Testing()
    Q_stored = np.load('Q_vals.npy')
    testing.test(Q_stored)