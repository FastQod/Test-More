from enum import auto
import pyautogui as pg
import time
check = pg.position()
print(check)
def drag():
    pg.moveTo(2087, 708 , 1)
    pg.dragTo(2087, 542 , 1, button='left')


#def autob():
    #pg.moveTo(453 ,345 ,1)#herosmenu
    #pg.leftClick()
    #pg.moveTo(210 ,161 ,1)#allwork
    #for c in range(10):
        #pg.leftClick()
    #pg.moveTo(279, 137 ,1) #exitherosmenu
    #pg.leftClick()
    #pg.moveTo(249, 228,1) #tshunt
    #pg.leftClick()
    #time.sleep(900)#1800
    #pg.moveTo(33,100,1) #exitwork
    #pg.leftClick()
    #pg.moveTo(453 ,345 ,1) #herosmenu
    #pg.leftClick()
    #pg.moveTo(236, 162,1) #exitrest
    #for c in range(10):
    #    pg.leftClick()
    #pg.moveTo(279, 137 ,1) #checkbcoin (222, 133 ,1)
    #pg.click()
    #pg.moveTo(472, 95,1) #exitcheckboin(472, 95,1)
    #pg.click()
    #time.sleep(1800)#7200,6800,5000
    #pg.moveTo(386, 138,1)
    #pg.click()


def autoclick():
    pg.moveTo(300,290)
    pg.click(300,290)
for i in range(100):
    time.sleep(900)
    autoclick()
















