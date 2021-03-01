#!/usr/bin/env python3
import os
import pygame
import random
import sys

WIDTH = 1060
HEIGHT = 480
FPS = 60




# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kokos")
clock = pygame.time.Clock()  # For syncing the FPS
b
# group all the sprites together for ease of update





class Kokos:
    def __init__(self):
        self.score = 0
        self.image = pygame.image.load(os.path.join('kokos.JPG')).convert()
        self.rect = self.image.get_rect() # use image extent values
        self.rect.topleft = [0, 0] # put the ball in the top left corner
        self.image = pygame.transform.rotozoom(self.image, 80, 0.18)
    def moveVertical(self, y):
        isHigherHeight = self.rect.y
        isHigherHeight += y
        if isHigherHeight >= HEIGHT or isHigherHeight <= 0:
            return
        self.rect.y += y
    def moveHoriztonal(self, x):
        isWiderWidth = self.rect.x
        isWiderWidth += x
        if isWiderWidth >= WIDTH or isWiderWidth <= 0:
            return
        self.rect.x += x

    def draw(self, surface):
        self.image = pygame.transform.scale(self.image, (100, 100))
        surface.blit(self.image, (self.rect.x, self.rect.y))

class GodisBit:
    def __init__(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        self.taken = False
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

# Game loop
running = True

nams = []

for i in range(0,30):
    nams.append(GodisBit())

kokos = Kokos()


while running:

    # 1 Process input/events
    clock.tick(FPS)  # will make the loop run at the same speed all the time
    # gets all the events which have occured till now and keeps tab of them.
    for event in pygame.event.get():
        # listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        kokos.moveHoriztonal(-10)
    if keys[pygame.K_RIGHT]:
        kokos.moveHoriztonal(10)
    if keys[pygame.K_UP]:
        kokos.moveVertical(-10)
    if keys[pygame.K_DOWN]:
        kokos.moveVertical(10)

    # 3 Draw/render
    screen.fill(BLACK)
    kokos.draw(screen)
    for i in nams:
        if pygame.Rect.colliderect(kokos.rect, i.rect):
            nams.remove(i)
        else:
            pygame.draw.rect(screen, (255, 255,255), i.rect)
    
    if len(nams) is 0:
        print("HEY")
        pygame.quit()
        sys.exit(0)
    ########################

    # Your code comes here

    ########################

    # Done after drawing everything to the screen
    pygame.display.flip()

pygame.quit()
