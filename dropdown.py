import pygame
from pygame import Rect

class rect_btn:
    def __init__(self, x:float, y:float, width:float, height:float, name:str, font_size:int, color:tuple =(255, 0, 0), hover_color:tuple = (150, 0, 0), txt_color:tuple=(255,255,255), txt_hover_color:tuple=(0, 0, 0)):
        self.x = x
        self.y = y
        self.w = width
        self.h = height

        self.name = name
        self.font_size = font_size
        self.o_color = txt_color
        self.txt_color = self.o_color
        self.t_hover_color = txt_hover_color

        self.color = color
        self.current_color = color
        self.hover_color = hover_color

        self.rect = Rect(self.x, self.y, self.w, self.h)
        self.clicked = False
        self.text_pos = [self.x + 5, self.y + 5]

    def show(self, screen):
        # check the cursor is hovering over the button
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.current_color = (150, 0, 0)
            self.txt_color = self.t_hover_color
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                self.clicked = False
        else:
            self.current_color = (255, 0, 0)
            self.txt_color = self.o_color

        pygame.draw.rect(screen, self.current_color, self.rect)
        self.text = screen.blit(pygame.font.SysFont(None, self.font_size).render(self.name, True, self.txt_color), (self.text_pos[0], self.text_pos[1]))
    
    def hover(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def changeFontSize(self, new_size: int):
        self.font_size = new_size

    # This funxtion allows you to move the text of the button around
    def moveTextBy(self, pos_change: tuple):
        self.text_pos[0] += pos_change[0]
        self.text_pos[1] += pos_change[1] 

class Dropdown:
    def __init__(self, x:int, y:int, btn_width:int, btn_height:int, names:list =[] ,content:list = [], color:tuple = (255, 0, 0), hover_color:tuple = (150, 0, 0)):
        self.x = x
        self.y = y
        self.btn_w = btn_width
        self.btn_h = btn_height

        self.content = content
        self.titles = names

        self.w = 20
        self.h = 20
        self.extended_height = 0
        self.color = color

        self.rect = Rect(self.x, self.y, self.w, self.h)

        for i in range(len(self.titles)):
            self.append(rect_btn((self.x + 10), (self.y + (self.btn_h * (i))) + 10, self.btn_w, self.btn_h, self.titles[i], 50))


    def append(self, btn):
        self.content.append(btn)

    def showContent(self, screen):
        for i in range(len(self.content)):
            self.content[i].show(screen)
            self.extended_height = self.content[i].h * (i + 1) + 20

    def show(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.showContent(screen)
            self.rect.w = self.btn_w + 20
            self.rect.h = self.extended_height
        else:
            self.rect.w = self.w
            self.rect.h = self.h
            # self.extended_height = 0

        pygame.draw.rect(screen, self.color, self.rect, 5, 3)

    
