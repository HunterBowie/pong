import windowgui, constants
import game


window = windowgui.Window(constants.SCREEN_SIZE)
window.set_manager(game.Game(window))
window.start(auto_cycle=True)