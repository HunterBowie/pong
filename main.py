import pygame
import windowgui, constants
import game

pygame.init()

window = windowgui.Window(constants.SCREEN_SIZE)
pygame.display.set_caption("Pong")

window.set_manager(game.Game(window))
window.start(auto_cycle=True)