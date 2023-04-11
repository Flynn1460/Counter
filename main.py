import pygame as pg, customLib as cl, time
import counter as c, dis_savedTypes as dm, ui

pg.font.init()

disWidth, disHeight = 600, 600
dis = pg.display.set_mode((disWidth, disHeight))

counter, timeLastOn, clickMultiplier, earningsPerSecond = c.parseCounterInfo(cl.file.readFile("assets/SavedScore.txt"))

offTimeSec = round(time.time()) - timeLastOn
counter += offTimeSec * earningsPerSecond

clickeeDonut = ui.clickThing("assets/donut.png", (disWidth//2, disHeight//2))
menuIcon = ui.clickThing("assets/menu.png", (70, 70))
menuPage = False

c.counterInit(40)
dm.disTypesInit(disWidth, disHeight)

clock = pg.time.Clock()

running = True
while running:
    if not menuPage:
        dm.clickMenu(dis, counter, clickeeDonut, menuIcon)

    else:
        clickMultiplier, earningsPerSecond, counter = dm.upgradesMenu(dis, menuIcon, clickMultiplier, earningsPerSecond, counter)
        menuPage = not menuIcon
    
    for event in pg.event.get():
        
        # If donut clicked update counter
        if clickeeDonut.updateClicks(event) and not menuPage:
            counter += clickMultiplier

        # Enter/exit the menu
        if menuIcon.updateClicks(event):
             menuPage = not menuPage
             print(menuPage)

        if event.type == pg.QUIT:
            c.endCounter(clickMultiplier, earningsPerSecond)
            running = False

    
    counter += earningsPerSecond / 60
    clock.tick(60)
    pg.display.update()