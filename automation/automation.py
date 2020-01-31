import pyautogui as p
import time

# print(p.size())

# absolute Position
# p.moveTo(100, 100, duration=0.25)

# relative Position
# for i in range(1):
#     p.move(200,0, duration=0.1)
#     p.move(0,100, duration=0.1)
#     p.move(-200,0, duration=0.1)
#     p.move(0,-100, duration=0.1)

# maus_pos = p.position()
# maus_pos.x = x Position
# maus_pos.y = y Position

# p.click() -> Linke Maustaste || Alternativ: p.click(x-pos, y-pos, button="left | right | middle")
# oder p.rightClick() | p.middleClick()
# p.mouseDown() -> Maustaste drücken ohne loslassen
# p.mouseUp() -> Maustatsen-Release
# Doppelklcick = p.doubleClick
# p.dragTo() -> Absolute Werte
# p.drag(x,y,duration) -> relative Werte

# p.pixel(x,y) RGB Farbe auslesen / return Value (R,G,B)
# p.pixelMatchesColor(x,y(R,G,B)) Schaut ob Pixelfarbe an X,Y mit gewollter Pixelfarbe (X,Y,Z) übereinstimmt

# p.locateOnScreen("imagename.dateiformat")  Return: Box(left=643, top=745, width=70, height=29)
# try:
#     location = pyautogui.locateOnScreen('submit.png')
# except:
#     print('Image could not be found.')
# Sinnvoll für locateOnScreen

# im = p.screenshot()
# print(p.pixel(50,200))

# console_button = p.locateOnScreen("img/console_button.png")
# p.click(console_button.left, console_button.top, button="left") # öffnet Konsole
# p.click("img/console_button.png")
# print(console_button)

# fw = p.getActiveWindow()
# fw
# Win32Window(hWnd=2034368)
# str(fw)
# '<Win32Window left="500", top="300", width="2070", height="1208", title="Mu 1.0.1 – test1.py">'
# fw.title
# 'Mu 1.0.1 – test1.py'
# fw.size
# (2070, 1208)
# fw.left, fw.top, fw.right, fw.bottom
# (500, 300, 2070, 1208)
# fw.topleft
# (256, 144)
# fw.area
# 2500560
# pyautogui.click(fw.left + 10, fw.top + 20)

# pyautogui.getAllWindows() Jedes Sichtbare Fenster
# pyautogui.getWindowsAt(x, y) jedes sichtbare Fenster dass auch in der X und Y Koordinate liegtg
# pyautogui.getWindowsWithTitle(title) Return eine Liste aller Fenster die (title) im WIndow Titelnamen hat
# pyautogui.getActiveWindow() returns aktives Fenster

print(p.getWindowsWithTitle("atom"))

def enter():
    p.hotkey('enter')

def firefox():
    p.hotkey('winleft','s')
    p.write('firefox')
    enter()
    p.getWindowsWithTitle('firefox')
    time.sleep(1)

def aktien():
    firefox()
    time.sleep(0.5)
    p.write('MSCI World')
    enter()

aktien()
