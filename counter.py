import pygame as pg, customLib as cl, time

def counterInit(fontSize):
    global font, text, rectWidth, rectHeight
    font = pg.font.Font("assets/Coconut Font.ttf", fontSize)

    text = font.render("0", True, (255, 255, 255))
    rectWidth, rectHeight = (text.get_rect().width)//2, (text.get_rect().height)//2

def counterUpdate(counter, center=False):
    global font, text, rectWidth, rectHeight, disCount, rawCounter

    rawCounter = counter
    disCount = cl.gen.commaNum(counter)

    text = font.render(disCount, True, (255, 255, 255))

    if center:
        rectWidth, rectHeight = (text.get_rect().width)//2, (text.get_rect().height)//2
    
    else:
        rectWidth, rectHeight = 0, 0

def counterDisplay(dis, x, y):
    dis.blit(text, (x, y, rectWidth, rectHeight))

def endCounter(data1, data2):
    global rawCounter
    disCount = str(rawCounter) + "\n" + str(int(time.time())) + "\n" + str(data1) + "\n" + str(data2)

    cl.file.writeFile("assets/SavedScore.txt", disCount)

def parseCounterInfo(counterInfo):
    counterInfo = counterInfo.split()

    return float(counterInfo[0]), int(counterInfo[1]), int(counterInfo[2]), int(counterInfo[3])