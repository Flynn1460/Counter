import pygame as pg
import counter as c, ui, customLib as cl

def disTypesInit(disWidth, disHeight):
    global dims
    dims = disWidth, disHeight




def clickMenu(dis, counter, clickeeDonut, menuIcon):
    dis.fill((229, 169, 169))

    c.counterUpdate(counter)
    c.counterDisplay(dis, 0, 0)

    clickeeDonut.blit(dis, 300, 300)
    menuIcon.blit(dis, dims[0], 0, center=False)


def upgradesMenu(dis, menuIcon, clickMultiplier, earningPerSec, counter):
    while True:
        dis.fill((83, 153, 135))
        menuIcon.blit(dis, dims[0], 0, center=False)

        donutChef = ui.upgradeCard("assets/dono_chef.png", (100, 100), "Well Trained Staff", "Cost: 100 ... +1 donuts per click")
        donutChef.blit(dis, (20, 20), center=False)

        parentHelp = ui.upgradeCard("assets/dono_chef.png", (100, 100), "Parental Donations", "Cost: 500 ... +1 donuts per second")
        parentHelp.blit(dis, (20, 130), center=False)

        doughContracts = ui.upgradeCard("assets/dono_chef.png", (100, 100), "Douzen Doughy Discounts", "Cost: 1000 ... +12 donuts per click")
        doughContracts.blit(dis, (20, 260), center=False)

        for event in pg.event.get():
            if donutChef.updateClicks(event) and counter >= 100:
                clickMultiplier += 1
                counter -= 100

            if parentHelp.updateClicks(event) and counter >= 500:
                earningPerSec += 1
                counter -= 500
            
            if doughContracts.updateClicks(event) and counter >= 1000:
                clickMultiplier += 12
                counter -= 1000

            if menuIcon.updateClicks(event):
                return clickMultiplier, earningPerSec, counter
            
            else:
                continue

        
        c.counterUpdate(counter)
        c.counterDisplay(dis, 300, 550)


        pg.display.update()

