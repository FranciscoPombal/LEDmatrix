import random
import socket
import sys
import time
import threading
from queue import Queue
from client.const import *


class Snake():
    def __init__(self, matrix, input_queue):
        self.matrix = matrix
        self.input_queue = input_queue
        self.snake_color = RED
        self.food_color = GREEN
        self.reset()
        self.loop()

    def reset(self):
        self.table = [[BLACK] * WIDTH for i in range(HEIGHT)]
        self.score = 0
        # initial snake position
        self.xs = [5, 5, 5, 5]
        self.ys = [6, 5, 4, 3]
        self.length = 4
        # initial apple position
        self.food = []
        self.food.extend(range(0, 2))
        self.food[0] = random.randint(0, WIDTH - 1)
        self.food[1] = random.randint(0, HEIGHT - 1)
        self.direction = DOWN
        self.changed = 1
        self.update_game()

    def update_screen(self):
        screen = b''
        for i in range(HEIGHT):
            for j in range(WIDTH):
                screen += bytes(self.table[i][j])

        self.matrix.sendall(screen)

    def update_game(self):
        self.table = [[BLACK]*WIDTH for x in range(HEIGHT)]

        # paint food squares
        self.table[self.food[1]][self.food[0]] = self.food_color

        # paint snake squares
        for i in range(self.length):
            self.table[self.ys[i]][self.xs[i]] = self.snake_color

        self.update_screen()

    def checkCollisionObject(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return True
        else:
            return False

    def checkCollisionWalls(self):
        if self.xs[0] >= 0 and self.xs[0] < WIDTH and self.ys[0] >= 0 and self.ys[0] < HEIGHT:
            return False
        else:
            return True

    def checkSelfCollision(self):
        for i in range(1, self.length):
            if self.checkCollisionObject(self.xs[0], self.ys[0], self.xs[i], self.ys[i]):
                return True
        return False

    def checkEatSnake(self):
        if self.checkCollisionObject(self.xs[0], self.ys[0], self.food[0], self.food[1]):
            self.xs.append(self.food[0])
            self.ys.append(self.food[1])
            self.length += 1

            # TODO: optimize. possiblepos can be created only once, and it can shrink as game progresses
            # TODO: still does not work for some reason
            possiblepos = []
            for i in range(HEIGHT):
                for j in range(WIDTH):
                    possiblepos.append((i, j))

            for i in range(0, self.length):
                possiblepos[self.ys[i] + (self.xs[i] * HEIGHT)] = (-1, -1)  # mark position as invalid

            possiblepos = sorted(possiblepos)
            possiblepos = possiblepos[self.length:]
            random.shuffle(possiblepos)
            newpos = possiblepos[random.randint(0, 200 - self.length - 1)]
            (self.food[1], self.food[0]) = newpos

    def moveSnake(self):
        xs_old = list(self.xs)
        ys_old = list(self.ys)
        for i in range(1, self.length):
            self.xs[i] = xs_old[i-1]
            self.ys[i] = ys_old[i-1]

        if self.direction == DOWN:
            self.ys[0] += 1
        elif self.direction == RIGHT:
            self.xs[0] += 1
        elif self.direction == UP:
            self.ys[0] -= 1
        elif self.direction == LEFT:
            self.xs[0] -= 1

    def loop(self):
        while True:
            if not self.input_queue.empty():
                btn = self.input_queue.get()

                if btn == 'Select':
                    break

                if self.changed == 0:
                    if btn == 'Up' and self.direction != DOWN:
                        self.direction = UP
                    elif btn == 'Down' and self.direction != UP:
                        self.direction = DOWN
                    elif btn == 'Left' and self.direction != 1:
                        self.direction = LEFT
                    elif btn == 'Right' and self.direction != LEFT:
                        self.direction = RIGHT
                    self.changed = 1

            self.checkEatSnake()
            self.moveSnake()
            self.changed = 0
            if self.checkCollisionWalls() or self.checkSelfCollision():
                break

            self.update_game()
            time.sleep(1/(3 + self.length/4))
