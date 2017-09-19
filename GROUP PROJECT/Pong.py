
__author__ = 'Charles Carper'


import pygame
import math
from pygame.locals import *
from random import random
from tkinter import *

###########################################################################################################
## Paddle Class
class Paddle():
  def __init__(self, screen, x, h):
    self.screen = screen
    (sw, sh) = screen.get_size()
    self.x = x - 10 #Changed 25 to 10, so both paddles are the same distance from the goal
    self.h = 125
    self.y = sh / 2 - self.h / 2
    self.w = 20
    self.max_y = sh - h
    self.min_y = 0
    self.speed = 0
    self.score = 0
###########################################################################################################
## move Function
  def move(self, amount):
    self.speed = amount
    self.y = self.y + amount
    if self.y > self.max_y:
        self.y = self.max_y
    elif self.y < self.min_y:
        self.y = self.min_y

###########################################################################################################
## score_point Function
  def score_point(self):
    self.score += 1

    #added goal text font - to appear after every time ball made a score
    if self.score <= 4:
        myfont = pygame.font.SysFont("monospace", 80)
        label = myfont.render("Goal!", 10, (255,255,255))
        self.screen.blit(label, (400, 100))
        pygame.display.flip()
        pygame.time.delay(1000)



###########################################################################################################
## Draw Function
  def draw(self):
    #the 3 sets of numbers, give the paddle different kinds of colors (change 255 to 100 for yellow paddles)
    pygame.draw.rect(self.screen, (255, 255, 100), (self.x, self.y, self.w, self.h))


###########################################################################################################
## Ball Class
class Ball():
  def __init__(self, screen):
    self.screen = screen
    self.w = 20
    self.h = 20
    self.playclick = False
    self.goal = pygame.mixer.Sound("goal.wav")
    self.speed = 15
    self.reset()

###########################################################################################################
## Reset Function
  def reset(self):
    (sw, sh) = self.screen.get_size()
    self.x = sw / 2 - 10
    self.y = sh / 2 - 5
    angle = random() * math.radians(20)
    self.dir_x = self.speed * math.cos(angle)
    self.dir_y = self.speed * math.sin(angle)
    if random() > 0.5:
      self.dir_x = -self.dir_x
    if random() > 0.5:
      self.dir_y = -self.dir_y
    self.timer = 3
###########################################################################################################

###########################################################################################################
## Update Function
  def update(self, time, p1, p2, ):
    if self.timer > 0:
      self.timer -= time
    else:
      self.x += self.dir_x
      self.y += self.dir_y
    (sw, sh) = self.screen.get_size()
    if self.x + 50 < 0:
      self.goal.play()
      p2.score_point()
###########################################################################################################
## Decision Structure
      if p2.score >= 5:
            screen = pygame.display.set_mode((1000, 800))
            font = pygame.font.Font(None, 48)
            text = font.render("Right Side Player Wins!", True, (255, 255, 255))
                                      #^^^ changed it to right side player, instead player 2
            text_x = 500 - text.get_rect().width / 2
            screen.blit(text, (text_x, 50))
            pygame.display.flip()
            pygame.time.delay(2000)
            p1.score = 0
            p2.score = 0
            self.reset()
      else:
        self.reset()
###########################################################################################################
    elif self.x > sw:
      self.goal.play()
      p1.score_point()

      if p1.score == 5:
            screen = pygame.display.set_mode((1000, 800))
            font = pygame.font.Font(None, 48)
            text = font.render("Left Side Player Wins!", True, (255, 255, 255))
                                   #^^^ changed it to left side player, instead player 1
            text_x = 500 - text.get_rect().width / 2
            screen.blit(text, (text_x, 50))
            pygame.display.flip()
            pygame.time.delay(2000)
            p1.score = 0
            p2.score = 0
            self.reset()
      else:
        self.reset()
    else:
      if (self.y < 0 and self.dir_y < 0) or (self.y + self.h > sh and self.dir_y > 0):
        self.dir_y = - self.dir_y
        self.playclick = True
      selfrect = pygame.Rect(self.x, self.y, self.w, self.h)
      p1rect = pygame.Rect(p1.x, p1.y, p1.w, p1.h)
      p2rect = pygame.Rect(p2.x, p2.y, p2.w, p2.h)
      if selfrect.colliderect(p1rect) and self.dir_x < 0:
        self.dir_x = -self.dir_x
        self.dir_y += p1.speed
        self.playclick = True
      elif selfrect.colliderect(p2rect) and self.dir_x > 0:
        self.dir_x = -self.dir_x
        self.dir_y += p2.speed
        self.playclick = True
      if self.dir_y > 15:
        self.dir_y = 15
      elif self.dir_y < -15:
        self.dir_y = -15
    
###########################################################################################################
## Draw Function
  def draw(self, font, click):

    pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.w, self.h))
    if self.timer > 0:
###########################################################################################################
## Formatting
      text = font.render("%.0f" % self.timer, True, (0, 0, 0))
###########################################################################################################
      text_x = self.x - text.get_rect().width / 2 + 10
      text_y = self.y - text.get_rect().height / 2 + 10
      self.screen.blit(text, (text_x, text_y))
    if self.playclick:
      click.play()
      self.playclick = False
          
          
###########################################################################################################
## Main Function
def main():
  pygame.init()
  pygame.mixer.init()
  pygame.mixer.music.load('background.wav')
  pygame.mixer.music.play(111, 0.0)
  pygame.mixer.music.set_volume(0.5)
  click = pygame.mixer.Sound("click.wav")
  screen = pygame.display.set_mode((1000, 800))
  clock = pygame.time.Clock()
  pygame.font.init()
  p1 = Paddle(screen, 100, 150)
  p2 = Paddle(screen, 900, 150)
  ball = Ball(screen)
  font = pygame.font.Font(None, 48)

#Text menu showing the control layouts and information
  text0 = font.render("Controls", True, (255, 255, 255))
  text0_x = 500 - text0.get_rect().width / 2
  screen.blit(text0, (text0_x, 50))
  text1 = font.render("Left Side Player: w = UP s = DOWN", True, (255, 255, 255))
  text1_x = 500 - text1.get_rect().width / 2
  screen.blit(text1, (text1_x, 90))
  text2 = font.render("Right Side Player: Up Arrow = UP Down Arrow = DOWN", True, (255, 255, 255))
  text2_x = 500 - text2.get_rect().width / 2
  screen.blit(text2, (text2_x, 130))
  text4 = font.render("Press the 'esc' key to EXIT", True, (255, 255, 255))#blank space
  text4_x = 500 - text4.get_rect().width / 2
  screen.blit(text4, (text4_x, 170))
  text3 = font.render("5 Points Wins the Match!", True, (255, 255, 255))#blank space
  text3_x = 500 - text3.get_rect().width / 2
  screen.blit(text3, (text3_x, 250))
  pygame.display.flip()
  pygame.time.delay(10000)

###########################################################################################################
## Repetition Structure
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
        sys.exit()
###########################################################################################################
###########################################################################################################
## Exception
    try:
        background_image = pygame.image.load("bg.png").convert()
###########################################################################################################
## List/Tuple
        screen.blit(background_image, [0, 0])
    except:
        print('An Error Has occurred.')
###########################################################################################################
###########################################################################################################
    keys = pygame.key.get_pressed()
    if keys[K_w] and not keys[K_s]: ## Move up
        p1.move(-20)
    if keys[K_s] and not keys[K_w]: ## Move down
        p1.move(20)
    if keys[K_UP] and not keys[K_DOWN]: ## Move up
        p2.move(-20)
    if keys[K_DOWN] and not keys[K_UP]:  ## Move Down
        p2.move(20)
    ball.update(1/60, p1, p2)
    p1.draw()
    p2.draw()
    ball.draw(font, click)
    text = font.render(str(p1.score) + "                                                         " + str(p2.score), True, (255, 255, 255))
    text_x = 500 - text.get_rect().width / 2
    screen.blit(text, (text_x, 50))
    pygame.display.flip()
    clock.tick(60)
if __name__ == "__main__":

  main()
