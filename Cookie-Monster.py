from PIL import ImageGrab, ImageOps
import pyautogui as pg
import time
from numpy import *
pg.FAILSAFE = True    # move mouse to top left of screen

class Cordinates():
    UpgradeBox = (1050, 210, 1350,735)
    app = (1250, 10)
    cookie = (200, 400)
    Cursor = (1200,230)
    Grandma = (1200, 320)
    Farm = (1200, 390)
    Mine = (1200, 440)
    Factory = (1200, 500)
    Bank = (1200,590)
    Temple = (1200, 640)
    WizardTower = (1200, 700)

def OpenApp():
    pg.click(Cordinates.app)

def CookieClick():
    pg.click(Cordinates.cookie)

def Upgrade():
    pg.click(Cordinates.Cursor)
    pg.click(Cordinates.Grandma)
    pg.click(Cordinates.Farm)
    pg.click(Cordinates.Mine)
    pg.click(Cordinates.Factory)
    pg.click(Cordinates.Bank)
    pg.click(Cordinates.Temple)
    pg.click(Cordinates.WizardTower)

def imagegrab():        # if an upgrade is avalible the sum will change
    box = Cordinates.UpgradeBox
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = array(greyImage.getcolors())
    x = a.sum()
    #print(x)
    return(x)

def main():
    OpenApp()
    while True:

       CookieClick()
       if imagegrab() != 173977:  # Whenever an upgrade is available it'll click
        Upgrade()
main()
