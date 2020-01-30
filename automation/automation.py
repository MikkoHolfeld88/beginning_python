import pyautogui as p
import time

print(p.size())

# absolute Position
p.moveTo(100, 100, duration=0.25)

# relative Position
# for i in range(1):
#     p.move(200,0, duration=0.1)
#     p.move(0,100, duration=0.1)
#     p.move(-200,0, duration=0.1)
#     p.move(0,-100, duration=0.1)

maus_pos = p.position()
# maus_pos.x = x Position
# maus_pos.y = y Position

# p.click() -> Linke Maustaste || Alternativ: p.click(x-pos, y-pos, button="left | right | middle")
# oder p.rightClick() | p.middleClick()
# p.mouseDown() -> Maustaste drücken ohne loslassen
# p.mouseUp() -> Maustatsen-Release
# Doppelklcick = p.doubleClick
# p.dragTo() -> Absolute Werte
# p.drag(x,y,duration) -> relative Werte
