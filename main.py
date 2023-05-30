import pygame
import sys

# 初始化pygame
pygame.init()
# 获取对显示系统的访问，并创建一个窗口screen
# 窗口大小为670x670
screen = pygame.display.set_mode((670, 670))
screen_color = [238, 154, 73]  # 设置画布颜色,[238,154,73]对应为棕黄色
line_color = [0, 0, 0]  # 设置线条颜色，[0,0,0]对应黑色

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
